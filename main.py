from telethon import TelegramClient, events
from vars import BOT_TOKEN

# 1. सबसे पहले Client को Define करें
api_id = 31911187
api_hash = '8291ae3d580f1fb5f8f84e0e3c6a3e6f'
client = TelegramClient('bot', api_id, api_hash).start(bot_token=BOT_TOKEN)

# 2. अब जब client बन गया है, उसके नीचे ही Events लिखें
@client.on(events.NewMessage)
async def handler(event):
    # आपका कोड यहाँ आएगा
    pass

client.run_until_disconnected()
