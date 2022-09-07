"""
MIT License

Copyright (c) 2022 Aʙɪsʜɴᴏɪ

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


import asyncio
from sys import version_info

from pyrogram import __version__ as pver
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telegram import __version__ as lver
from telethon import __version__ as tver

from Exon import BOT_NAME
from Exon import BOT_USERNAME as fuck
from Exon import OWNER_USERNAME, SUPPORT_CHAT, UPDATES_CHANNEL, pgram

ASAU = [
    [
        InlineKeyboardButton(text="ᴜᴘᴅᴀᴛᴇꜱ", url=f"https://t.me/{UPDATES_CHANNEL}"),
        InlineKeyboardButton(text="ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}"),
    ],
    [
        InlineKeyboardButton(
            text="Aᴅᴅ Mᴇ Iɴ Yᴏᴜʀ Gʀᴏᴜᴘ",
            url=f"https://t.me/{fuck}?startgroup=true",
        ),
    ],
]


@pgram.on_message(filters.command("alive"))
async def restart(client, m: Message):
    await m.delete()
    accha = await m.reply("⚡")
    await asyncio.sleep(1)
    await accha.edit("Aʟɪᴠɪɴɢ..")
    await asyncio.sleep(0.1)
    await accha.edit("Aʟɪᴠɪɴɢ Bᴀᴋᴀᴀ ....")
    await accha.delete()
    await asyncio.sleep(0.1)
    await m.reply_photo(
        reply.PHOTO(https://telegra.ph/file/45bdde838d8ba044de209.jpg)
        caption=f"""**Hᴇʏ, I Aᴍ {BOT_NAME}**
     ▱▱▱▱▱▱▱▱▱▱▱▱
❆ **Mʏ Mᴀsᴛᴇʀ :** [𝗝 𝗘 𝗔 𝗡](https://t.me/{OWNER_USERNAME})
❆ **Lɪʙʀᴀʀʏ Vᴇʀsɪᴏɴ :** `{lver}`
❆ **Tᴇʟᴇᴛʜᴏɴ Vᴇʀsɪᴏɴ :** `{tver}`
❆ **Pʏʀᴏɢʀᴀᴍ Vᴇʀsɪᴏɴ :** `{pver}`
❆ **Pʏᴛʜᴏɴ Vᴇʀsɪᴏɴ :** `{version_info[0]}.{version_info[1]}.{version_info[2]}`
❆ **Bᴏᴛ Vᴇʀꜱɪᴏɴ :** `1.0`
     ▱▱▱▱▱▱▱▱▱▱▱▱""",
        reply_markup=InlineKeyboardMarkup(ASAU),
    )
