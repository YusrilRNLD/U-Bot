# Copyright (C) 2020 Catuserbot <https://github.com/sandy1709/catuserbot>
# Ported by @mrismanaziz
# Reupdate From @merdhni

import asyncio
from datetime import datetime
from io import BytesIO

from telethon.errors import BadRequestError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import Channel

import userbot.modules.sql_helper.gban_sql as gban_sql
from userbot import BOTLOG_CHATID
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, DEVS, DEVG, ramblacklist
from userbot.events import register
from userbot.utils import chataction, edit_or_reply, edit_delete, get_user_from_event, ram_cmd

from .admins import BANNED_RIGHTS, UNBAN_RIGHTS

ehajg = edit_delete

async def admin_groups(grp):
    admgroups = []
    async for dialog in grp.client.iter_dialogs():
        entity = dialog.entity
        if (
            isinstance(entity, Channel)
            and entity.megagroup
            and (entity.creator or entity.admin_rights)
        ):
            admgroups.append(entity.id)
    return admgroups


def mentionuser(name, userid):
    return f"[{name}](tg://user?id={userid})"


@ram_cmd(pattern="gban(?: |$)(.*)")
@register(pattern=r"^\.cgban(?: |$)(.*)", sudo=True)
async def gban(event):
    if event.fwd_from:
        return
    gbun = await edit_or_reply(event, "`Memulai Global Banned...`")
    start = datetime.now()
    user, reason = await get_user_from_event(event, gbun)
    if not user:
        return
    if user.id == (await event.client.get_me()).id:
        await ehajg(event, "**Kurang Kerjaan Amat Gban diri Sendiri Goblok lo...**", 5)
        return
    if user.id in DEVS:
        await ehajg(event, "**Maaf Kak, Lo Gabisa Gban dia Karna Dia Developer Gua**", 5)
        return
    if user.id in DEVG:
        await ehajg(event, "**Maaf Kak, Itu admin Gua, Lo Gabisa Gban Dia Tolol...**", 5)
        return
    if gban_sql.is_gbanned(user.id):
        await gbun.edit(
            f"**Si** [TOLOL](tg://user?id={user.id}) **ini sudah ada di daftar gbanned**"
        )
    else:
        gban_sql.freakgban(user.id, reason)
    san = []
    san = await admin_groups(event)
    count = 0
    fiz = len(san)
    if fiz == 0:
        await gbun.edit("**Gabisa Gban, Karna Lo gada Gc Yg Lo adminin....**")
        return
    await gbun.edit(
        f"**Global Banned Si** [TOLOL](tg://user?id={user.id}) **Dalam** `{len(san)}` **groups**"
    )
    for i in range(fiz):
        try:
            await event.client(EditBannedRequest(san[i], user.id, BANNED_RIGHTS))
            await asyncio.sleep(0.5)
            count += 1
        except BadRequestError:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"**Anda tidak memiliki izin Banned di :**\n**Group Chat :** `{event.chat_id}`",
            )
    end = datetime.now()
    timetaken = (end - start).seconds
    if reason:
        await gbun.edit(
            f"**Global Banned Si** [{user.first_name}](tg://user?id={user.id}) **Dalam** `{count}` **grup, Dengan** `{timetaken}` **seconds**!!\n**Alasan :** `{reason}`"
        )
    else:
        await ehajg(event,
            f"**Global Banned Si** [{user.first_name}](tg://user?id={user.id}) **Dalam** `{count}` **grup, Dengan** `{timetaken}` **seconds**!!\n**Terdaftar Dalam List Gban.**", 5
        )


@ram_cmd(pattern="ungban(?: |$)(.*)")
@register(pattern=r"^\.cungban(?: |$)(.*)", sudo=True)
async def ungban(event):
    if event.fwd_from:
        return
    ungbun = await edit_or_reply(event, "`Membatalkan Global Banned...`")
    start = datetime.now()
    user, reason = await get_user_from_event(event, ungbun)
    if not user:
        return
    if gban_sql.is_gbanned(user.id):
        gban_sql.freakungban(user.id)
    else:
        await ungbun.edit(
            f"**SI** [TOLOL](tg://user?id={user.id}) **INI BELOM LO GBAN ANJING!!!!!!!!!**"
        )
        return
    san = []
    san = await admin_groups(event)
    count = 0
    fiz = len(san)
    if fiz == 0:
        await ungbun.edit("**Gabisa Ungban, Karna Lo ga ada gc yg lo adminin....**")
        return
    await ungbun.edit(
        f"**Membatalkan perintah Global Banned Untuk Si** [TOLOL](tg://user?id={user.id}) **Dalam** `{len(san)}` **groups**"
    )
    for i in range(fiz):
        try:
            await event.client(EditBannedRequest(san[i], user.id, UNBAN_RIGHTS))
            await asyncio.sleep(0.5)
            count += 1
        except BadRequestError:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"**Anda tidak memiliki izin Banned di :**\n**Group Chat :** `{event.chat_id}`",
            )
    end = datetime.now()
    timetaken = (end - start).seconds
    if reason:
        await ungbun.edit(
            f"**Membatalkan Perintah Global Banned** [{user.first_name}](tg://user?id={user.id}`) **Dalam** `{count}` **Grup, Dengan** `{timetaken}` **Detik**!!\n**Alasan :** `{reason}`"
        )
    else:
        await ehajg(event,
            f"**Membatalkan Perintah Global Banned** [{user.first_name}](tg://user?id={user.id}) **Dalam** `{count}` **Grup, Dengan** `{timetaken}` **Detik**!!\n**Menghapus Dari Daftar Global Banned**", 5
        )


@ram_cmd(pattern="listgban$")
async def gablist(event):
    await edit_or_reply(event, "**Sebentar Gua Ambil list nya....**")
    if event.fwd_from:
        return
    gbanned_users = gban_sql.get_all_gbanned()
    GBANNED_LIST = "**DAFTAR MANUSIA SAMPAH!!!**\n\n"
    if len(gbanned_users) > 0:
        for a_user in gbanned_users:
            if a_user.reason:
                GBANNED_LIST += f"✨ User ID: [{a_user.chat_id}](tg://user?id={a_user.chat_id})\n└ Alasan: {a_user.reason}\n\n"
            else:
                GBANNED_LIST += f"✨ User ID: [{a_user.chat_id}](tg://user?id={a_user.chat_id})\n└ Tanpa Alasan\n\n"
    else:
        GBANNED_LIST = "LO BELOM GBAN ORANG ANJING!!!"
    if len(GBANNED_LIST) > 4096:
        with BytesIO(str.encode(GBANNED_LIST)) as fileuser:
            fileuser.name = "list-gban.text"
            await event.client.send_file(
                event.chat_id,
                fileuser,
                force_document=True,
                thumb="userbot/utils/styles/RAMUBOT.jpg",
                caption="**List Global Banned**",
                reply_to=event.reply_to_msg_id,
                allow_cache=False,
            )
            await event.delete()
    else:
        await edit_or_reply(event, GBANNED_LIST)


@chataction()
async def _(event):
    if event.user_joined or event.added_by:
        user = await event.get_user()
        chat = await event.get_chat()
        if gban_sql.is_gbanned(user.id) and ramblacklist and chat.admin_rights:
            try:
                await event.client.edit_permissions(
                    chat.id,
                    user.id,
                    view_messages=False,
                )
                await event.reply(
                    f"**✨GBanned_User** Bergabung.\n\n** • Nama:** [{user.first_name}](tg://user?id={user.id})\n • **Aksi:** `Banned`"
                )
            except BaseException:
                pass



CMD_HELP.update(
    {
        "gban": f"**Plugin : **`gban`\
        \n\n  •  **Syntax :** `{cmd}gban` <username/id>\
        \n  •  **Function : **Melakukan Banned Secara Global Ke Semua Grup Dimana anda Sebagai Admin.\
        \n\n  •  **Syntax :** `{cmd}ungban` <username/id>\
        \n  •  **Function : **Membatalkan Global Banned\
        \n\n  •  **Syntax :** `{cmd}listgban`\
        \n  •  **Function : **Menampilkan List Global Banned\
    "
    }
)
