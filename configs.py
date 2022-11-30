# (c) @KGN_OFFICIAL

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 7588344))
    API_HASH = os.environ.get("API_HASH", "6ade175bcf8ea4981e3153ef48fe07f5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "MdiskSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    BOT_OWNER = int(os.environ.get("BOT_OWNER"))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL"),( None)
    PORT = os.environ.get("PORT","8080")
    ABOUT_BOT_TEXT = """<b>This is Mdisk Search Bot.
    


🤖 My Name: <a href='https://t.me/FilmyFather_BotList'>Mdisk Search Robot</a>

📝 Language : <a href='https://www.python.org'> Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'> Pyrogram</a>

📡 Server: <a href='https://heroku.com'>Heroku</a>

👨‍💻 USED IN: <a href='https://t.me/blackest_harbour'>Req GROUP </a></b>
"""

    ABOUT_HELP_TEXT = """<b>👨‍💻 : <a href='https://t.me/sigma_male_007'>Developer</a>

If You Want Your Own Bot Like This Then You Can Contact Our Developer.</b>
"""

    HOME_TEXT = """
<b>Hey! {}😅,

I'm Mdisk Search Robot.🤖</a>

I Can Search!🔍 What You Want?😜

<a>Made With ❤ </a></b>
"""


    START_MSG = """
<b>Hey! {}😅,

I'm Mdisk Search Robot.🤖</a>

I Can Search!🔍 What You Want?😜

<a>Made With ❤ </a></b>
"""


