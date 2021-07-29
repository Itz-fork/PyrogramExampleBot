# Pyrogram Example Bot
This is an example telegram bot writtn in **Python** using **Pyrogram** 

# Deploying The Bot

## Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Itz-fork/PyrogramExample)

## On VPS / Pc
**Before Doing Anything Install Python 3! To Install It [Click Here](https://www.python.org/downloads/)**

```bash
# To Clone This Repo
git https://github.com/Itz-fork/PyrogramExampleBot

# Fill Configs with your own values in config.py

# To Enter The Folder
cd PyrogramExampleBot

# To Install Requirements
pip3 install -r requirements.txt

# To Run the bot using below command
python3 -m TheBot
```

# Making More Commands

If you need more commands,

### For Commands That Works On Both Private and Group

[Go Here](https://github.com/Itz-fork/PyrogramExampleBot/blob/6b91ba651368c06ec87554991f191a82a6d02763/TheBot/plugins/start.py) Then Start Typing [From This Line](https://github.com/Itz-fork/PyrogramExampleBot/blob/6b91ba651368c06ec87554991f191a82a6d02763/TheBot/plugins/start.py#L13)! Then Type Lines Till [This Line](https://github.com/Itz-fork/PyrogramExampleBot/blob/6b91ba651368c06ec87554991f191a82a6d02763/TheBot/plugins/start.py#L40)

```python
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
```

**Replace @Pyro_Tg_Bot with your bot username in commands!**


### For Commands That Works Only On Private

[Go Here](https://github.com/Itz-fork/PyrogramExampleBot/blob/6b91ba651368c06ec87554991f191a82a6d02763/TheBot/plugins/start.py) Then Start Typing [From This Line](https://github.com/Itz-fork/PyrogramExampleBot/blob/6b91ba651368c06ec87554991f191a82a6d02763/TheBot/plugins/start.py#L45)! Then Type Lines Till [This Line](https://github.com/Itz-fork/PyrogramExampleBot/blob/6b91ba651368c06ec87554991f191a82a6d02763/TheBot/plugins/start.py#L64)

```python
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
```

# Note

Made for beginners like me to learn some very basic things (Made with Love) 😊
Please don't copy paste cuz i made this for learning! Not for copy pasting!

After 1 or 2 months (Actually Can't Remember Tho 😅) I realize Copy Pasting can't make a programmer So Don't Copy Paste :) 😄

Will Add Some Extra Thing When I Have Time 😇! Currently Busy 😃

# Support
<a href="https://t.me/Nexa_bots"><img src="https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white"></a>

# Credits
<a href="https://github.com/pyrogram/pyrogram"><img src="https://img.shields.io/badge/Pyrogram-E34F26?style=for-the-badge"></a>
