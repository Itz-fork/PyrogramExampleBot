# Copyright ( c ) 2021 Itz-fork
# Made for beginners like me to learn some very basic things {Made with Love}
# Me sometimes suck at coding so PR's welcome

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

# Bot will works both private & public because we don't filter chat private or group (Lol huh?)

@Client.on_message(filters.command(["start", "start@nexamusicbot"]))
async def start(_, message: Message):
    await message.reply_text(
        f"""<b>Selam {message.from_user.first_name} 😉️!</b>

Merak etme çalışıyorum:)

Beni kontrol etmeye geldiğin için teşekkürler.❤️

Ama şu anda bakım aşamasındayım.🛠️

Bitince Mükemmel Bir Bot Olacağına eminim🌟

🌠İstersen geliştiricinin duyuru yapacağı AylakBot's kanalına abone olup değişiklirden ilk haberdar olan kişi olabilirsin.🌠
 
 🔥Ya da sohbet etmek istersen **@TheLucii**'in sohbet grubuna gelebilirsin.🔥
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔰️ Güncelleme Kanalı 🔰️", url="https://t.me/AylakXBots"
                    ),
                    InlineKeyboardButton(
                        "⚜️ Luci'nin Mekanı ⚜️", url="https://t.me/LuciChat"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "👑Sahip👑", url="https://t.me/ayiak"
                    )
                ]
            ]
        )
    )


# So now let's make private only command

@Client.on_message(filters.command(["repo", "repo@nexamusicbot"]) & filters.private)
async def repo(_, message: Message):
    await message.reply_text(
        f"""<b>Selam {message.from_user.first_name} 😉️!</b>

🛠️Bakımdayım😣""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "👑Sahip👑", url="https://t.me/ayiak"
                    )
                ]
            ]
        )
    )

    
# Finally a Callback

# First lemme make a seperate private command for that

@Client.on_message(filters.command(["help", "helpb@nexamusicbot"]) & filters.private)
async def help(_, message: Message):
    await message.reply_text(
        f"""<b>Selam {message.from_user.first_name}</b>

😞Bakımdayım🛠️!

""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "👑Sahip👑", url="https://t.me/ayiak"
                    )
                ]
            ]
        )
    )


# 
