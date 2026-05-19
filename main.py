from pyrogram import Client
from vars import BOT_TOKEN

# in_memory=True करने से कोई .session फाइल नहीं बनेगी
app = Client(
    "my_bot",
    bot_token=BOT_TOKEN,
    in_memory=True 
)

print("बोट सफलता के साथ लाइव हो गया है!")
app.run()
