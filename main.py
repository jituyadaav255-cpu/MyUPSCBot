from telethon import TelegramClient
from vars import BOT_TOKEN

# अपनी असली डिटेल्स यहाँ डालें
api_id = 31911187
api_hash = '8291ae3d580f1fb5f8f84e0e3c6a3e6f'

# बोट स्टार्ट करें
client = TelegramClient('bot', api_id, api_hash).start(bot_token=BOT_TOKEN)

print("बोट सफलता के साथ लाइव हो गया है!")
client.run_until_disconnected()
