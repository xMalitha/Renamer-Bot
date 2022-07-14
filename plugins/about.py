
from pyrogram import Client, filters


@Client.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	await message.reply_text("🎊 Bot :- @rename_alphabot\n 👨‍💻 Creater :- <tg-spoiler>@xMalitha </tg-spoiler>\n🎁 Language :-Python3\n🎨 Library :- Pyrogram 1.4.16\n💫 Server :- Heroku")
