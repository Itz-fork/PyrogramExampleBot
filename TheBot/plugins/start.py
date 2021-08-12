# Copyright ( c ) 2021 Itz-fork
# Made for beginners like me to learn some very basic things {Made with Love}
# Me sometimes suck at coding so PR's welcome

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

# Bot will works both private & public because we don't filter chat private or group (Lol huh?)

@Client.on_message(filters.command(["start", "start@Pyro_Tg_Bot"]))
async def start(_, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name} 😉️!</b>

Heya I'm Alive :)

Made by **@Bruh_0x** for Noob/Beginners Like Him!

Join **@NexaBotsUpdates**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔰️ My Updates Channel 🔰️", url="https://t.me/NexaBotsUpdates"
                    ),
                    InlineKeyboardButton(
                        "⚜️ Support Group ⚜️", url="https://t.me/Nexa_bots"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Follow On Github", url="https://github.com/Itz-fork"
                    )
                ]
            ]
        )
    )


# So now let's make private only command

@Client.on_message(filters.command(["repo", "repo@Pyro_Tg_Bot"]) & filters.private)
async def repo(_, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name} 😉️!</b>

Kk Click On The Below Button For The Repo :)

Made by **@Bruh_0x** for Noob/Beginners Like Him!

Join **@NexaBotsUpdates**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Repo", url="https://github.com/Itz-fork/PyrogramExampleBot"
                    )
                ]
            ]
        )
    )

    
# Finally a Callback

# First lemme make a seperate private command for that

@Client.on_message(filters.command(["testcb", "testcb@Pyro_Tg_Bot"]) & filters.private)
async def testcb(_, message: Message):
    await message.reply_text(
        f"""<b>Hey This is a test command!</b>

Click On Below Button To See How Callback Works!

Join **@NexaBotsUpdates**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Click Me Please!", callback_data="testcallback"
                    )
                ]
            ]
        )
    )


# Callback data
# You can replace "testcallback" with your callback name!
# If you have big callback stuff like 100+ lines you can make a seperate py file for that! In SAME DIR.

@Client.on_callback_query(filters.regex("testcallback"))
async def testcallback(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>Congrats! You Clicked On a Calllback Button!</b>

This is how callbacks works! Have a Great Day!

Made with ❤️ <b>@NexaBotsUpdates</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Repo", url="https://github.com/Itz-fork/PyrogramExampleBot"
                    )
                ]
            ]
        )
    )
