from pyrogram import Client
from vars import BOT_TOKEN
app = Client("my_bot", bot_token=BOT_TOKEN)
print("बोट लाइव है!")
app.run()
