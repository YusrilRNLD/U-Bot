# From vckyou Geez-Userbot
# WOI NGENTOT, KALO FORK KASIH BINTANG
# Yang apus kredit Lo ngentot!

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import CMD_HANDLER as cmd, CMD_HELP
from userbot.utils import edit_or_reply, ram_cmd
from userbot.events import register


@ram_cmd(pattern="limit(?: |$)(.*)")
@register(pattern=r"^\.clim(?: |$)(.*)", sudo=True)
async def _(event):
    xx = await edit_or_reply(event, f"`Jangan panik lah tolol, Yahahah ngentod...`")
    async with event.client.conversation("@SpamBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=178220800)
            )
            await conv.send_message("/start")
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.client(UnblockRequest("@SpamBot"))
            await conv.send_message("/start")
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        await xx.edit(f"~ {response.message.message}")


CMD_HELP.update({"limit": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}limit`"
                 "\n•: ngecek akun kena limit atau gak"})
