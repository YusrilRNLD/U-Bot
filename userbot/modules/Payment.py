# Copyright (C) YusrilRNLD
# -Ubot < https://github.com/yusrilrnld/ubot >
# ReEdit by @YUSRIL4YOU
# All rights reserved.
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.

from userbot import CMD_HELP, CMD_HANDLER as cmd

from userbot.events import register

from userbot.utils import ram_cmd

# ================= CONSTANT =================

#                FROM U-BOT

# ============================================

@register(outgoing=True, pattern='^pay(?: |$)(.*)')

async def _(typew):

    await typew.client.send_message(

        typew.chat_id, "** PAYMENT ACENG • STOREE VIA DANA = 0895611203477 VIA GOPAY = 081270603368 **", reply_to=typew.reply_to_msg_id)
 
    await typew.delete()

CMD_HELP.update({

    "Payments":

   f"pay or `{cmd}payment`\

\nUsage: Untuk Menunjukkan Pembayaran.\

})
