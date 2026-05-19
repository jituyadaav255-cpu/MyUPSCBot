from telethon import TelegramClient
from vars import BOT_TOKEN

# Telethon के लिए API_ID और HASH की जरूरत नहीं होती अगर आप सिर्फ बोट टोकन यूज़ कर रहे हैं
# यहाँ API_ID में 12345 और HASH में कोई भी रैंडम स्ट्रिंग डाल दें, यह बस एक फॉर्मेलिटी है
api_id = 12345
api_hash = '0123456789abcdef0123456789abcdef'

client = TelegramClient('bot', api_id, api_hash).start(bot_token=BOT_TOKEN)

print("बोट सफलता के साथ लाइव हो गया है!")
client.run_until_disconnected()
