from telethon import TelegramClient, events
import yt_dlp
import os

api_id = 31911187
api_hash = '8291ae3d580f1fb5f8f84e0e3c6a3e6f'
bot_token = '8908901463:AAHuKRv0wbGys3TOHNO7tElnv8Gl75G6cRk'

client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage)
async def process_file(event):
    if event.message.file and event.message.file.name.endswith('.txt'):
        await event.respond("फाइल मिल गई! लिंक निकाल रहा हूँ...")
        path = await event.download_media()
        
        with open(path, 'r') as f:
            links = f.readlines()

        for link in links:
            link = link.strip()
            if link.startswith('http'):
                try:
                    await event.respond(f"डाउनलोड कर रहा हूँ: {link}")
                    # yt-dlp का उपयोग करके डाउनलोड करें
                    ydl_opts = {'outtmpl': 'video.mp4', 'format': 'best'}
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([link])
                    
                    # टेलीग्राम पर भेजें
                    await event.client.send_file(event.chat_id, 'video.mp4')
                    os.remove('video.mp4') # फाइल भेजने के बाद डिलीट करें
                except Exception as e:
                    await event.respond(f"एरर आया: {str(e)}")
        
        os.remove(path)
        await event.respond("काम पूरा हुआ!")

print("बोट अब लिंक प्रोसेस करने के लिए तैयार है!")
client.run_until_disconnected()
