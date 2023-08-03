from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://shadow:BE_XB@cluster0.noovm8n.mongodb.net/?retryWrites=true&w=majority")

OWNER_ID = int(getenv("OWNER_ID", 6199134030))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/spzohary")
