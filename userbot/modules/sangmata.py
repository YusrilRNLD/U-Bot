# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
# Port to userbot by @MoveAngel

import asyncio

from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, DEVS
from userbot.utils import (
    _format,
    edit_delete,
    edit_or_reply,
    get_user_from_event,
    ram_cmd,
)


@ram_cmd(pattern="sm(s)?(?:\s|$)([\s\S]*)")
async def _(event):
    input_str = "".join(event.text.split(maxsplit=1)[1:])
    reply_message = await event.get_reply_message()
    if not input_str and not reply_message:
        await edit_delete(event, "`Reply ke pesan seseorang lah Bangsat....`", 10)
    user, rank = await get_user_from_event(event, secondgroup=True)
    if not user:
        return
    if user.id in DEVS:
        await edit_delete(event, "`Lu gabisa telusuri nama dia, Karna dia developer gua tod 😏`", 10)
        return
    uid = user.id
    chat = "@SangMataInfo_bot"
    sangevent = await edit_or_reply(event, "`Lu siapa si kentot, Kepo Gua, Ga terima? Pc.....`")
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message(f"/search_id {uid}")
        except YouBlockedUserError:
            await event.client(UnblockRequest(chat))
            await conv.send_message(f"/search_id {uid}")
        responses = []
        while True:
            try:
                response = await conv.get_response(timeout=2)
            except asyncio.TimeoutError:
                break
            responses.append(response.text)
        await event.client.send_read_acknowledge(conv.chat_id)
    if not responses:
        await edit_delete(sangevent, "**Wah si anjing Belom pernah ganti nama nih bangsat....**", 10)
    if "No records found" in responses:
        await edit_delete(sangevent, "**Gua pantau pantau, Romannya belom ganti Nama ni orang....**", 10)
    names, usernames = await sangamata_seperator(responses)
    cmd = event.pattern_match.group(1)
    rama = None
    check = usernames if cmd == "s" else names
    for i in check:
        if rama:
            await event.reply(i, parse_mode=_format.parse_pre)
        else:
            rama = True
            await sangevent.edit(i, parse_mode=_format.parse_pre)


async def sangamata_seperator(sanga_list):
    for i in sanga_list:
        if i.startswith("🔗"):
            sanga_list.remove(i)
    s = 0
    for i in sanga_list:
        if i.startswith("Username History"):
            break
        s += 1
    usernames = sanga_list[s:]
    names = sanga_list[:s]
    return names, usernames


CMD_HELP.update(
    {
        "sangmata": f"**Plugin : **`sangmata`\
        \n\n  •  **Syntax :** `{cmd}sm` <sambil reply chat>\
        \n  •  **Function : **Mendapatkan Riwayat Nama Pengguna selama di telegram.\
        \n\n  •  **Syntax :** `{cmd}sms` <sambil reply chat>\
        \n  •  **Function : **Mendapatkan Riwayat Username Pengguna selama di telegram.\
    "
    }
)
