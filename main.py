import yt_dlp # इसे इस्तेमाल करने के लिए requirements.txt में 'yt-dlp' लिखें
from telethon import events

@client.on(events.NewMessage)
async def handle_txt_file(event):
    if event.message.file and event.message.file.name.endswith('.txt'):
        path = await event.download_media()
        
        # फाइल पढ़कर लिंक निकालें
        with open(path, 'r') as f:
            links = f.readlines()
            
        for link in links:
            # yt-dlp का इस्तेमाल करके वीडियो डाउनलोड करें
            ydl_opts = {'format': 'best', 'outtmpl': 'video.mp4'}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link.strip()])
            
            # वीडियो वापस टेलीग्राम पर भेजें
            await event.respond(file='video.mp4')
