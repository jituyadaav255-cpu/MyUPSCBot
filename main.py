from telethon import TelegramClient, events
import yt_dlp

# 1. सबसे पहले Client को Define करें
api_id = 31911187
api_hash = '8291ae3d580f1fb5f8f84e0e3c6a3e6f'
bot_token = '8908901463:AAHuKRv0wbGys3TOHNO7tElnv8Gl75G6cRk'

client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

# 2. अब जब client बन चुका है, तब ये Event Handlers लिखें
@client.on(events.NewMessage(pattern='/start'))
async def start_handler(event):
    await event.respond('नमस्ते! मैं आपका UPSC बोट हूँ।')

@client.on(events.NewMessage)
async def file_handler(event):
    if event.message.file and event.message.file.name.endswith('.txt'):
        await event.respond("फाइल मिल गई, प्रोसेस कर रहा हूँ...")

# 3. अंत में रन करें
print("बोट सफलतापूर्वक शुरू हो गया है!")
client.run_until_disconnected()
