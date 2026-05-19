from telethon import TelegramClient, events
import yt_dlp
import os

api_id = 31911187
api_hash = '8291ae3d580f1fb5f8f84e0e3c6a3e6f'
bot_token = '8908901463:AAHuKRv0wbGys3TOHNO7tElnv8Gl75G6cRk'

client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage)
async def downloader_handler(event):
    if event.message.file and event.message.file.name.endswith('.txt'):
        await event.respond("फाइल मिल गई! लिंक प्रोसेस कर रहा हूँ...")
        path = await event.download_media()
        
        with open(path, 'r', encoding='utf-8') as f:
            links = f.readlines()

        for link in links:
            url = link.strip()
            if url.startswith('http'):
                try:
                    await event.respond(f"कोशिश कर रहा हूँ: {url}")
                    ydl_opts = {'outtmpl': 'downloaded_video.mp4', 'format': 'best'}
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([url])
                    
                    if os.path.exists('downloaded_video.mp4'):
                        await event.client.send_file(event.chat_id, 'downloaded_video.mp4')
                        os.remove('downloaded_video.mp4')
                    else:
                        await event.respond("यह लिंक डाउनलोड नहीं हो सका।")
                except Exception as e:
                    await event.respond(f"इस लिंक में एरर है: {str(e)}")
        
        os.remove(path)
        await event.respond("सभी लिंक्स प्रोसेस हो गए!")

print("बोट अब काम शुरू कर रहा है!")
client.run_until_disconnected()
