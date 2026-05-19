from pyrogram import Client
from vars import BOT_TOKEN

# API_ID और HASH को None पर सेट करना सबसे जरूरी है
# ताकि बोट सिर्फ TOKEN का इस्तेमाल करे
app = Client(
    "my_bot",
    api_id=None,
    api_hash=None,
    bot_token=BOT_TOKEN
)

print("बोट शुरू हो रहा है...")
app.run()
