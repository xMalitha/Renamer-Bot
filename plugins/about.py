
from pyrogram import Client, filters


@Client.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	await message.reply_text("š Bot :- @_______\n šØāš» Creater :- <tg-spoiler>@xMalitha </tg-spoiler>\nš Language :-Python3\nšØ Library :- Pyrogram 1.4.16\nš« Server :- Heroku")
