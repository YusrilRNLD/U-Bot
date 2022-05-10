from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.utils import edit_or_reply as tolol, ram_cmd as tod
from userbot import bot, CMD_HELP, CMD_HANDLER as cmd


@tod(pattern="gid(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await tolol(event, "`Mohon Balas Ke Pesan Ngentot!!`")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await tolol(event, "```Mohon Balas Ke Pesan Ngentot!!```")
        return
    chat = "@getidsbot"
    reply_message.sender
    if reply_message.sender.bot:
        await tolol(event, "`Mohon Balas Ke Pesan ngentot!!`")
        return
    await tolol(event, "`Mencari ID.......`")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=186675376))
            await bot.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await tolol(event, "`Bot Sedang Error`")
            return
        if response.text.startswith("Forward"):
            await tolol(event, "`Pengguna Ini Tidak Mempunyai ID`")
        else:
            await tolol(event, f"{response.message.message}")


CMD_HELP.update({
    "getid":
    f"`{cmd}gid`"
    "\nUsage: Balas Ke Pesan Pengguna Untuk Mendapatkan ID Nya."
})
