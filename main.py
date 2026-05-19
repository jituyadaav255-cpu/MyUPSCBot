from telethon import TelegramClient, events
from vars import BOT_TOKEN

api_id = 31911187
api_hash = '8291ae3d580f1fb5f8f84e0e3c6a3e6f'
client = TelegramClient('bot', api_id, api_hash).start(bot_token=BOT_TOKEN)

# 1. /start का जवाब देने के लिए
@client.on(events.NewMessage(pattern='/start'))
async def start_handler(event):
    await event.respond('नमस्ते! मुझे कोई भी .txt फाइल भेजें, मैं उसे पढ़कर उसका कंटेंट बता दूंगा।')

# 2. फाइल पढ़ने और उसका कंटेंट भेजने के लिए
@client.on(events.NewMessage)
async def file_handler(event):
    if event.message.file and event.message.file.name.endswith('.txt'):
        # फाइल डाउनलोड करें
        path = await event.download_media()
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read(1000) # शुरू के 1000 शब्द पढ़ेंगे ताकि टेलीग्राम पर बड़ा एरर न आए
            await event.respond(f"फाइल का कंटेंट है:\n\n{content}")

print("बोट फाइल पढ़ने के लिए तैयार है!")
client.run_until_disconnected()
