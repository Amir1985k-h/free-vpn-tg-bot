import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")          # عدد منفی مثل -1001234567890
CHANNEL_USERNAME = os.getenv("CHANNEL_USERNAME")  # بدون @
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

# تنظیمات ربات
BOT_USERNAME = "yourbot"  # بدون @
