from pyrogram import Client
import os

# vars.py की जगह सीधे यहाँ से टोकन लें अगर मुमकिन हो, 
# या फिर vars से ही उठाएं
from vars import BOT_TOKEN

# api_id और api_hash को हटाकर सिर्फ bot_token दें
app = Client(
    "bot",
    bot_token=BOT_TOKEN
)

print("बोट लाइव हो रहा है...")
app.run()
