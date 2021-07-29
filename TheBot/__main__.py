# ( c ) Bruh_0x
# Made for beginners like me to learn some very basic things {Made with Love}
# Me sometimes suck at coding so PR's welcome

# Please don't copy paste cuz i made this for learning! Not for copy pasting! 
# I realize Copy Pasting can't make a programmer So Don't Copy Paste :)

from pyrogram import Client, idle
from config import Config


if __name__ == "__main__" :
    plugins = dict(root="TheBot/plugins")
    app1 = Client(
        "Client1",
        bot_token=Config.BOT_TOKEN1,
        api_id=Config.APP_ID1,
        api_hash=Config.API_HASH1,
        plugins=plugins
    )
    app2 = Client( # This is 2nd client. add much as you wish. but remember to edit starting process
        "Client2",
        bot_token=Config.BOT_TOKEN2,
        api_id=Config.APP_ID1,
        api_hash=Config.API_HASH1,
        plugins=plugins
    )
    print("Waking Up Client 1")
    app1.start() # Starting Client 1
    print("Waking Up Client 2")
    app2.start() # Starting Client 2
    print("Everything Ok! Enjoy Multi Client! Lol!") # Remove this shit if you like lmao
    idle()
