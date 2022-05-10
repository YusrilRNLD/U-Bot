from telethon.tl.functions.channels import LeaveChannelRequest as bangke

from userbot import BLACKLIST_CHAT, BLACKLIST_GCAST as Anj
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import edit_or_reply, ram_cmd as lol
from userbot.events import register as gblk
from .gcast import GCAST_BLACKLIST as Mekih


@lol(pattern="exit$", allow_sudo=False)
@gblk(pattern="^\.cexit$", sudo=True)
async def kickme(event):
    if event.chat_id in BLACKLIST_CHAT:
        return await edit_or_reply(
            event, "**LO GABISA GUNAKAN DISINI NGENTOD!!**"
        )
    user = await event.client.get_me()
    await edit_or_reply(event, f"`{user.first_name} Keluar Dari grup, Karna haram gc nya!!`")
    await event.client.kick_participant(event.chat_id, "me")


@lol(pattern="leaved$", allow_sudo=False)
async def kikme(event):
    if event.chat_id in BLACKLIST_CHAT:
        return await edit_or_reply(
            event, "**LO GABISA GUNAIN DISINI ANJING!!!!**"
        )
    await edit_or_reply(event, "**GC JELEK BGINI ANJING, MENDING GUA CABUT!!** 🥴")
    await event.client.kick_participant(event.chat_id, "me")


@lol(pattern="exitall$", allow_sudo=False)
@gblk(pattern="^\.exits$", sudo=True)
async def kickmeall(event):
    Ram = await edit_or_reply(event, "`Saat Nya keluar Dari seluruh Group.....`")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            if chat not in Mekih and chat not in Anj:
                try:
                    done += 1
                    await event.client(bangke(chat))
                except BaseException:
                    er += 1
    await Ram.edit(
        f"**Berhasil Keluar dari {done} Group, Gagal Keluar dari {er} Group**"
    )


CMD_HELP.update(
    {
        "kickme": f"**Plugin : **`kickme`\
        \n\n  •  **Syntax :** `{cmd}exit`\
        \n  •  **Function : **Keluar grup\
        \n\n  •  **Syntax :** `{cmd}leaved`\
        \n  •  **Function : **Keluar grup dengan menampilkan pesan Toxic 🥴\
    "
    }
)

CMD_HELP.update(
    {
        "exitall": f"**Plugin : **`exitall`\
        \n\n  •  **Syntax :** `{cmd}exitall`\
        \n  •  **Function : **Keluar dari semua grup telegram yang anda gabung.\
        \n\n  •NOTE: Berhati hatilah Dalam menggunakan fitur {cmd}exitall, Karna Itu Berbahaya.\
    "
    }
)
