# Ping From <\ram-ubot/>
# From @lahsiajg <starboy/>

""" Userbot module containing commands related to the \
    Information Superhighway (yes, Internet). """

import asyncio
import random
import time
from datetime import datetime

from speedtest import Speedtest

from userbot import CMD_HANDLER as cmd
from userbot.utils import edit_or_reply, ram_cmd
from userbot import CMD_HELP, BOT_VER, DEVG, REPO_NAME, StartTime, branch
from userbot.events import register

gesss = [
    "Eh ada Owner keren",
    "Hadir ganteng 😍",
    "Hi Tuan, kemana sj? 🤗",
    "Hadir kak 😉",
    "Hadir bang 😁",
    "Hadir bang maap telat 🥺",
    "Saya slalu ada buat Tuan Owner🥵",
    "Jangan kemana mana lagi ya bang",
    "Pas banget bang, aku lagi kangen",
    "Bang owner on juga akhirnya🥵",
]

brb = [
    "Bang owner mau off.",
    "Jangan off dong bang.",
    "Bang, mau kemana?",
    "Jangan lama lama bang",
    "Siap bang.",
    "Yah udah off aja bang.",
    "Off lagi, mau ngewe ya?",
    "Bang developer, lagi ange kah? ",
    "Jangan lupa makan bang.",
    "Yah pasti mao bucin ni.",
    "Jangan off terus lah bang.",
    "Mau nonton bokep kah?",
    "Bang Ganteng telah off.",
]

async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["Dtk", "Mnt", "Jam", "Hari"]

    while count < 4:
        count += 50
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@register(incoming=True, from_users=DEVG, pattern=r"^gesss$")
async def _(landak):
    await landak.reply(random.choice(gesss))


@register(incoming=True, from_users=1826643972, pattern=r"^brb$")
async def _(landak):
    await landak.reply(random.choice(brb))

@ram_cmd(pattern="ping$")
async def _(ping):
    """ For.ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await ping.client.get_me()
    await ping.client.send_message(
        ping.chat_id, f"**╰•★★ |rค๓ ρꪮꪀᧁ| ★★•╯**\n"
                    f"★ **speed:** "
                    f"`%sms` \n"
                    f"★ **Uptime:** "
                    f"`{uptime}` \n"
                    f"★ **owner:** [{user.first_name}](tg://user?id={user.id})\n" % (duration), reply_to=ping.reply_to_msg_id)
    await ping.delete()

@ram_cmd(pattern="rping$")
@register(pattern=r"^\.cping(?: |$)(.*)", sudo=True)
async def _(pong):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    ram = await edit_or_reply(pong, "**Mengecek Sinyal...**")
    await ram.edit("**▁**")
    await ram.edit("**▁ ▂**")
    await ram.edit("**▁ ▂ ▄**")
    await ram.edit("**▁ ▂ ▄ ▅**")
    await ram.edit("**▁ ▂ ▄ ▅ ▆**")
    await ram.edit("**▁ ▂ ▄ ▅ ▆ ▇**")
    await ram.edit("**▁ ▂ ▄ ▅ ▆ ▇ █**")
    await ram.edit("**▁ ▂ ▄ ▅ ▆ ▇**")
    await ram.edit("**▁ ▂ ▄ ▅ ▆**")
    await ram.edit("**▁ ▂ ▄ ▅ **")
    await ram.edit("**▁ ▂ ▄**")
    await ram.edit("**▁ ▂**")
    await ram.edit("**▁**")
    await ram.edit("**▁ ▂**")
    await ram.edit("**▁ ▂ ▄**")
    await ram.edit("**▁ ▂ ▄ ▅**")
    await ram.edit("**▁ ▂ ▄ ▅ ▆**")
    await ram.edit("**▁ ▂ ▄ ▅ ▆ ▇**")
    await ram.edit("**▁ ▂ ▄ ▅ ▆ ▇ █**")
    await asyncio.sleep(1)
    await ram.edit("✨")
    await asyncio.sleep(3)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await pong.client.get_me()
    await pong.client.send_message(
        pong.chat_id, f"**🌟𝗥𝗔𝗠-𝗨𝗕𝗢𝗧🌟**\n"
                     f"** ➠  Sɪɢɴᴀʟ   :** "
                     f"`%sms` \n"
                     f"** ➠  Bᴏᴛᴠᴇʀ  :** "
                     f"`{BOT_VER}` \n"
                     f"** ➠  Uᴘᴛɪᴍᴇ  :** "
                     f"`{uptime}` \n"
                     f"** ➠  Oᴡɴᴇʀ   :** [{user.first_name}](tg://user?id={user.id})" % (duration), reply_to=pong.reply_to_msg_id)
    await pong.delete()

@ram_cmd(pattern="pink$")
async def redis(pong):
    """For .ping command, ping the userbot from any chat."""
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    ram = await edit_or_reply(pong, "**𓀐.....................................𓂸**")
    await ram.edit("**𓀐..................................𓂸..**")
    await ram.edit("**𓀐................................𓂸....**")
    await ram.edit("**𓀐..............................𓂸......**")
    await ram.edit("**𓀐............................𓂸........**")
    await ram.edit("**𓀐..........................𓂸..........**")
    await ram.edit("**𓀐.......................𓂸.............**")
    await ram.edit("**𓀐.....................𓂸...............**")
    await ram.edit("**𓀐...................𓂸.................**")
    await ram.edit("**𓀐..................𓂸..................**")
    await ram.edit("**𓀐................𓂸....................**")
    await ram.edit("**𓀐..............𓂸......................**")
    await ram.edit("**𓀐............𓂸........................**")
    await ram.edit("**𓀐..........𓂸..........................**")
    await ram.edit("**𓀐........𓂸............................**")
    await ram.edit("**𓀐.......𓂸.............................**")
    await ram.edit("**𓀐....𓂸...............................**")
    await ram.edit("**𓀐..𓂸.................................**")
    await ram.edit("**𓀐.𓂸..................................**")
    await ram.edit("**𓀐𓂸...................................**")
    await ram.edit("**𓀐.𓂸..................................**")
    await ram.edit("**𓀐𓂸...................................**")
    await ram.edit("**𓀐.𓂸..................................**")
    await ram.edit("**𓂺**")
    await asyncio.sleep(2)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user= await pong.client.get_me()
    await pong.client.send_message(
        pong.chat_id, f"**➾ OWNER      :** [{user.first_name}](tg://user?id={user.id}) \n"
                     f"**➾ Kecepatan : ** %sms  \n"
                     f"**➾ Branch       : ** [{branch}] \n" % (duration), reply_to=pong.reply_to_msg_id) 
    await pong.delete()

@ram_cmd(pattern="speed$")
async def speedtst(spd):
    """ For .speed command, use SpeedTest to check server speeds. """
    await spd.edit("`Menjalankan Tes Kecepatan Jaringan, Mohon Tunggu...✨`")
    test = Speedtest()

    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()

    await spd.edit("**Kecepatan Jaringan:\n**"
                   "✧ **Dimulai Pada :** "
                   f"`{result['timestamp']}` \n"
                   f" **━━━━━━━━━━━━━━━━━**\n\n"
                   "✧ **Download:** "
                   f"`{speed_convert(result['download'])}` \n"
                   "✧ **Upload:** "
                   f"`{speed_convert(result['upload'])}` \n"
                   "✧ **Signal:** "
                   f"`{result['ping']}` \n"
                   "✧ **ISP:** "
                   f"`{result['client']['isp']}` \n"
                   f"✧ **BOT:** {REPO_NAME}")


def speed_convert(size):
    """
    Hi human, you can't read bytes?
    """
    power = 2**10
    zero = 0
    units = {0: '', 1: 'Kb/s', 2: 'Mb/s', 3: 'Gb/s', 4: 'Tb/s'}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"


@ram_cmd(pattern="pong$")
async def pingme(pong):
    """For .ping command, ping the userbot from any chat."""
    start = datetime.now()
    ram = await edit_or_reply(pong, "`Pong...........🐎`")
    await ram.edit("`Pong..........🐎.`")
    await ram.edit("`Pong.........🐎..`")
    await ram.edit("`Pong........🐎...`")
    await ram.edit("`Pong.......🐎....`")
    await ram.edit("`Pong......🐎.....`")
    await ram.edit("`Pong.....🐎......`")
    await ram.edit("`Pong....🐎.......`")
    await ram.edit("`Pong...🐎........`")
    await ram.edit("`Pong..🐎.........`")
    await ram.edit("`Pong.🐎..........`")
    await ram.edit("`Pong🐎...........`")
    end = datetime.now()
    duration = (end - start).microseconds / 9000
    user= await pong.client.get_me()
    await pong.client.send_message(
        pong.chat_id, f"**✨Oᴡɴᴇʀ : [{user.first_name}](tg://user?id={user.id})**\n📗 `%sms`" % (duration), reply_to=pong.reply_to_msg_id)
    await pong.delete()

CMD_HELP.update({
    "ping": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}ping` or `{cmd}rping` or `{cmd}pink`\
         \n↳ : Untuk Menunjukkan Ping Bot Anda.\
         \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}speed`\
         \n↳ : Untuk Menunjukkan Kecepatan Jaringan Anda.\
         \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}pong`\
         \n↳ : Sama Seperti Perintah {cmd}pink."})
