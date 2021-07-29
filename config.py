import os

class Config(object):
    BOT_TOKEN1 = os.environ.get("BOT_TOKEN1", "")
    APP_ID1 = int(os.environ.get("APP_ID1", ""))
    API_HASH1 = os.environ.get("API_HASH1", "")
    BOT_TOKEN2 = os.environ.get("BOT_TOKEN2", "")
