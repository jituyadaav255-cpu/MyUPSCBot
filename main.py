from telethon import TelegramClient, events
from vars import BOT_TOKEN

api_id = 31911187
api_hash = '8291ae3d580f1fb5f8f84e0e3c6a3e6f'

client = TelegramClient('bot', api_id, api_hash).start(bot_token=BOT_TOKEN)

# यह कोड बोट को कमांड सुनने में मदद करेगा
@client.on(events.NewMessage(pattern='/start'))
async def start_handler(event):
    await event.respond('नमस्ते! मैं UPSC कनवर्टर बोट हूँ। मैं आपकी कैसे मदद कर सकता हूँ?')

print("बोट मैसेज सुनने के लिए तैयार है!")
client.run_until_disconnected()
