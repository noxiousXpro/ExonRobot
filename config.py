from os import getenv

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    LOGGER = True

    API_ID = int(getenv("API_ID", 24269862))
    API_HASH = getenv("API_HASH", None)
    ARQ_API_KEY = "PMPTTD-HOMLMF-SRBHNH-RZMWXL-ARQ"
    SPAMWATCH_API = None
    TOKEN = getenv("TOKEN", "7090415113:AAH2QcjJEzUO0irZFlPStqoChaxuLjKEZUk")
    OWNER_ID = int(getenv("OWNER_ID", "5154912723"))
    OWNER_USERNAME = getenv("OWNER_USERNAME", "NoxiousXpro")
    SUPPORT_CHAT = getenv("SUPPORT_CHAT", "NoxBots")
    LOGGER_ID = int(getenv("LOGGER_ID", "-1002052189895"))
    MONGO_URI = getenv(
        "MONGO_DB_URI",
        "mongodb+srv://b7604190:hii121itsk@cluster0.vtt1cxt.mongodb.net/?retryWrites=true&w=majority",
    )
    DB_NAME = getenv("DB_NAME", "ExonRobot")
    REDIS_URL = "redis://default:wK6ZCiclq4iQKYpgfY90v6kd6WdPfEwl@redis-10186.c263.us-east-1-2.ec2.cloud.redislabs.com:10186/default"
    DATABASE_URL = getenv("DATABASE_URL", None)

    # ɴᴏ ᴇᴅɪᴛ ᴢᴏɴᴇ
    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://")


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
