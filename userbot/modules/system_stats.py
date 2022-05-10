# System Stats RAM-UBOT

import asyncio
import time
from asyncio import create_subprocess_exec as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
from platform import python_version, uname
from shutil import which
from os import remove
from telethon import version
from telethon import __version__, version
from pytgcalls import __version__ as pytgcalls
import platform
import sys
import time
from datetime import datetime
import psutil
from userbot.events import register
from userbot import ALIVE_LOGO, CMD_HELP, GROUP_LINK, CH_SFS, IG_ALIVE, EMOJI_HELP, RAM_TEKS_KOSTUM, REPO_NAME, BOT_VER, branch, StartTime, bot
from userbot import CMD_HANDLER as cmd
from userbot.utils import ram_cmd

# ================= CONSTANT =================
aliver = RAM_TEKS_KOSTUM
emo = EMOJI_HELP
grup = GROUP_LINK
modules = CMD_HELP
# ============================================



async def get_readable_time(seconds: int) -> str: 
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["Dtk", "Mnt", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(
            seconds, 60) if count < 3 else divmod(
            seconds, 24)
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


@ram_cmd(pattern=r"spc")
async def psu(event):
    uname = platform.uname()
    softw = "**Informasi Sistem**\n"
    softw += f"`Sistem   : {uname.system}`\n"
    softw += f"`Rilis    : {uname.release}`\n"
    softw += f"`Versi    : {uname.version}`\n"
    softw += f"`Mesin    : {uname.machine}`\n"
    # Boot Time
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    softw += f"`Waktu Hidup: {bt.day}/{bt.month}/{bt.year}  {bt.hour}:{bt.minute}:{bt.second}`\n"
    # CPU Cores
    cpuu = "**Informasi CPU**\n"
    cpuu += "`Physical cores   : " + \
        str(psutil.cpu_count(logical=False)) + "`\n"
    cpuu += "`Total cores      : " + \
        str(psutil.cpu_count(logical=True)) + "`\n"
    # CPU frequencies
    cpufreq = psutil.cpu_freq()
    cpuu += f"`Max Frequency    : {cpufreq.max:.2f}Mhz`\n"
    cpuu += f"`Min Frequency    : {cpufreq.min:.2f}Mhz`\n"
    cpuu += f"`Current Frequency: {cpufreq.current:.2f}Mhz`\n\n"
    # CPU usage
    cpuu += "**CPU Usage Per Core**\n"
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
        cpuu += f"`Core {i}  : {percentage}%`\n"
    cpuu += "**Total CPU Usage**\n"
    cpuu += f"`Semua Core: {psutil.cpu_percent()}%`\n"
    # RAM Usage
    svmem = psutil.virtual_memory()
    memm = "**Memori Digunakan**\n"
    memm += f"`Total     : {get_size(svmem.total)}`\n"
    memm += f"`Available : {get_size(svmem.available)}`\n"
    memm += f"`Used      : {get_size(svmem.used)}`\n"
    memm += f"`Percentage: {svmem.percent}%`\n"
    # Bandwidth Usage
    bw = "**Bandwith Digunakan**\n"
    bw += f"`Unggah  : {get_size(psutil.net_io_counters().bytes_sent)}`\n"
    bw += f"`Download: {get_size(psutil.net_io_counters().bytes_recv)}`\n"
    help_string = f"{str(softw)}\n"
    help_string += f"{str(cpuu)}\n"
    help_string += f"{str(memm)}\n"
    help_string += f"{str(bw)}\n"
    help_string += "**Informasi Mesin**\n"
    help_string += f"`Python {sys.version}`\n"
    help_string += f"`Telethon {__version__}`"
    await event.edit(help_string)


def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


@ram_cmd(pattern=r"sysd$")
async def sysdetails(sysd):
    if not sysd.text[0].isalpha() and sysd.text[0] not in ("/", "#", "@", "!"):
        try:
            fetch = await asyncrunapp(
                "neofetch",
                "--stdout",
                stdout=asyncPIPE,
                stderr=asyncPIPE,
            )

            stdout, stderr = await fetch.communicate()
            result = str(stdout.decode().strip()) + \
                str(stderr.decode().strip())

            await sysd.edit("`" + result + "`")
        except FileNotFoundError:
            await sysd.edit("`Install neofetch first !!`")


@ram_cmd(pattern=r"botver$")
async def bot_ver(event):
    if event.text[0].isalpha() or event.text[0] in ("/", "#", "@", "!"):
        return
    if which("git") is not None:
        ver = await asyncrunapp(
            "git",
            "describe",
            "--all",
            "--long",
            stdout=asyncPIPE,
            stderr=asyncPIPE,
        )
        stdout, stderr = await ver.communicate()
        verout = str(stdout.decode().strip()) + str(stderr.decode().strip())

        rev = await asyncrunapp(
            "git",
            "rev-list",
            "--all",
            "--count",
            stdout=asyncPIPE,
            stderr=asyncPIPE,
        )
        stdout, stderr = await rev.communicate()
        revout = str(stdout.decode().strip()) + str(stderr.decode().strip())

        await event.edit(
            "**☛**RAM-UBOT Versi:** \n "
            f"{verout}"
            "\n**☛**Revisi:**\n "
            f"{revout}"
        )
    else:
        await event.edit(
            "Sayang sekali anda tidak memiliki git, Anda Menjalankan Bot - 'v1.beta.4'!"
        )


@ram_cmd(pattern=r"pip(?: |$)(.*)")
async def pipcheck(pip):
    if pip.text[0].isalpha() or pip.text[0] in ("/", "#", "@", "!"):
        return
    pipmodule = pip.pattern_match.group(1)
    if pipmodule:
        await pip.edit("`Mencari...`")
        pipc = await asyncrunapp(
            "pip3",
            "search",
            pipmodule,
            stdout=asyncPIPE,
            stderr=asyncPIPE,
        )

        stdout, stderr = await pipc.communicate()
        pipout = str(stdout.decode().strip()) + str(stderr.decode().strip())

        if pipout:
            if len(pipout) > 4096:
                await pip.edit("`Output Terlalu Besar, Dikirim Sebagai File`")
                file = open("output.txt", "w+")
                file.write(pipout)
                file.close()
                await pip.client.send_file(
                    pip.chat_id,
                    "output.txt",
                    reply_to=pip.id,
                )
                remove("output.txt")
                return
            await pip.edit(
                "**Query: **\n`"
                f"pip3 search {pipmodule}"
                "`\n**Result: **\n`"
                f"{pipout}"
                "`"
            )
        else:
            await pip.edit(
                "**Query: **\n`"
                f"pip3 search {pipmodule}"
                "`\n**Result: **\n`No Result Returned/False`"
            )
    else:
        await pip.edit("Gunakan `.help pip` Untuk Melihat Contoh")


@ram_cmd(pattern=r"(?:alive|on)\s?(.)?")
async def amireallyalive(alive):
    user = await alive.client.get_me()
    uptime = await get_readable_time((time.time() - StartTime))
    output = (
        f"**[RAM-UBOT](https://github.com/ramadhani892/RAM-UBOT) Update dan berjalan.**\n\n"
        f"**╭✠╼━━━━━━❖━━━━━━━✠╮**\n"
        f"       **{aliver}**\n"
        f"**╰✠╼━━━━━━❖━━━━━━━✠╯**\n\n"
        f"▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰\n"
        f"{emo} **Master :** [{user.first_name}](tg://user?id={user.id}) \n"
        f"{emo} **Modules :** `{len(modules)} Modules` \n"
        f"{emo} **Bot Version :** `{BOT_VER}` \n"
        f"{emo} **Python Version :** `{python_version()}` \n"
        f"{emo} **Pytgcalls Version :** `{pytgcalls.__version__}` \n"
        f"{emo} **Telethon Version :** `{version.__version__}` \n"
        f"{emo} **Bot Uptime :** `{uptime}` \n"
        f"{emo} **Branch     :** `[{branch}]` \n"
        f"    **[𝗦𝘂𝗽𝗽𝗼𝗿𝘁]({GROUP_LINK})** | **[𝗖𝗵𝗮𝗻𝗻𝗲𝗹]({CH_SFS})** | **[𝗢𝘄𝗻𝗲𝗿](tg://user?id={user.id})**\n"
        f"▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰"
    )
    if ALIVE_LOGO:
        try:
            logo = ALIVE_LOGO
            await alive.delete()
            msg = await bot.send_file(alive.chat_id, logo, caption=output)
            await asyncio.sleep(50)
            await msg.delete()
        except BaseException:
            await alive.edit(
                output + "\n\n *`The provided logo is invalid."
                "\nMake sure the link is directed to the logo picture`"
            )
            await asyncio.sleep(100)
            await alive.delete()
    else:
        await alive.edit(output)
        await asyncio.sleep(100)
        await alive.delete()

@ram_cmd(pattern=r"(?:ralive|ron)\s?(.)?")
async def amireallyalive(alive):
    user = await bot.get_me()
    await get_readable_time((time.time() - StartTime))
    output = (
        f"**╭✠╼━━━━━━❖━━━━━━━✠╮**\n"
        f"       **♕  ⭐️𝗥𝗔𝗠-𝗨𝗕𝗢𝗧⭐️  ♕** \n"
        f"**╰✠╼━━━━━━❖━━━━━━━✠╯**\n"
        f"❃ **Tuan**             ➥ `{user.first_name}` \n"
        f"❃ **Username**    ➥ `@{user.username}` \n"
        f"❃ **Telethon**       ➥ `Versi {version.__version__}` \n"
        f"❃ **Python**          ➥ `Versi {python_version()}` \n"
        f"❃ **Versi Bot**      ➥ `{BOT_VER}` \n"
        f"❃ **Modul**           ➥ `{len(modules)}` \n\n"
        f"**▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰**\n"
        f"[{REPO_NAME}](https://github.com/ramadhani892/RAM-UBOT) || [𝗚𝗥𝗢𝗨𝗣]({GROUP_LINK}) || [𝗜𝗡𝗦𝗧𝗔𝗚𝗥𝗔𝗠]({IG_ALIVE})\n"
        f"**▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰ **")
    if ALIVE_LOGO:
        try:
            logo = ALIVE_LOGO
            await alive.delete()
            msg = await bot.send_file(alive.chat_id, logo, caption=output)
            await asyncio.sleep(50)
            await msg.delete()
        except BaseException:
            await alive.edit(
                output + "\n\n *`The provided logo is invalid."
                "\nMake sure the link is directed to the logo picture`"
            )
            await asyncio.sleep(100)
            await alive.delete()
    else:
        await alive.edit(output)
        await asyncio.sleep(100)
        await alive.delete()


@ram_cmd(pattern=r"(?:ram|rambot)\s?(.)?")
@register(pattern=r"^\.(?:clive|on)\s?(.)?", sudo=True)
async def amireallyalive(alive):
    user = await bot.get_me()
    await get_readable_time((time.time() - StartTime))
    await alive.edit("`Perkenalan diri...⭐`")
    await asyncio.sleep(1)
    await alive.edit("✨")
    await asyncio.sleep(2)
    output = (
        f"**✠╼━━━━━━❖━━━━━━━✠ ** \n"
        f"**          ⭐️𝗥𝗔𝗠-𝗨𝗕𝗢𝗧⭐️** \n"
        f"**✠╼━━━━━━❖━━━━━━━✠** \n"
        f"╭✠╼━━━━━━❖━━━━━━━✠╮ \n"
        f"┣|• `{emo} Majikan  :`{user.first_name} \n"
        f"┣|• `{emo} Username :`@{user.username} \n"
        f"┣|• `{emo} Telethon :`Ver {version.__version__} \n"
        f"┣|• `{emo} tgcalls  :`Ver {pytgcalls.__version__} \n"
        f"┣|• `{emo} Python   :`Ver {python_version()} \n"
        f"╰✠╼━━━━━━❖━━━━━━━✠╯ \n"
        f"╭✠╼━━━━━━❖━━━━━━━✠╮ \n"
        f"┣|• `Branch      :`{branch} \n"
        f"┣|• `Bot Ver     :`{BOT_VER} \n"
        f"┣|• `Modules     :`{len(modules)} Modules \n"
        f"╰✠╼━━━━━━❖━━━━━━━✠╯ \n"
        f"▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰ \n"
        f"[{REPO_NAME}](https://github.com/ramadhani892/RAM-UBOT) || [𝐆𝐑𝐎𝐔𝐏]({GROUP_LINK}) || [𝐈𝐍𝐒𝐓𝐀𝐆𝐑𝐀𝐌]({IG_ALIVE}) \n"
        f"▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰")
    if ALIVE_LOGO:
        try:
            logo = ALIVE_LOGO
            await alive.delete()
            msg = await bot.send_file(alive.chat_id, logo, caption=output)
            await asyncio.sleep(50)
            await msg.delete()
        except BaseException:
            await alive.edit(
                output + "\n\n *`Logo Yang Disediakan Tidak Valid."
                "\nPastikan Tautan Yang Anda Gunakan Valid`"
            )
            await asyncio.sleep(100)
            await alive.delete()
    else:
        await alive.edit(output)
        await asyncio.sleep(100)
        await alive.delete()


@ram_cmd(pattern=r"aliveu")
async def amireallyaliveuser(username):
    message = username.text
    output = ".aliveu [new user without brackets] nor can it be empty"
    if message != ".aliveu" and message[7:8] == " ":
        newuser = message[8:]
        global DEFAULTUSER
        DEFAULTUSER = newuser
        output = "Successfully changed user to " + newuser + "!"
    await username.edit("`" f"{output}" "`")


@ram_cmd(pattern=r"resetalive$")
async def amireallyalivereset(ureset):
    global DEFAULTUSER
    DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
    await ureset.edit("`" "Successfully reset user for alive!" "`")


CMD_HELP.update({
    "sistem":
    f"`{cmd}sysd`\
\nUsage: Shows system information using neofetch.\
\n\n`{cmd}botver`\
\nUsage: Shows the userbot version.\
\n\n`{cmd}pip` <module(s)>\
\nUsage: Does a search of pip modules(s).\
\n\n`{cmd}start`\
\nUsage: Type .start to see whether your bot is working or not.\
\n\n`{cmd}aliveu` <text>\
\nUsage: Changes the 'user' in alive to the text you want.\
\n\n`{cmd}resetalive`\
\nUsage: Resets the user to default.\
\n\n`{cmd}db`\
\nUsage:Shows database related info.\
\n\n`{cmd}spc`\
\nUsage:Show system specification."
})
