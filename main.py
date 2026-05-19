from telethon import TelegramClient, events
import yt_dlp
import os
from vars import API_ID, API_HASH, BOT_TOKEN

# =========================
# Start Bot
# =========================

client = TelegramClient(
    'bot',
    API_ID,
    API_HASH
).start(bot_token=BOT_TOKEN)

print("✅ Bot Started Successfully")

# =========================
# TXT File Handler
# =========================

@client.on(events.NewMessage)

async def txt_handler(event):

    if event.message.file and event.message.file.name.endswith('.txt'):

        await event.respond(
            "✅ TXT File मिल गई\n🎬 Video Download शुरू..."
        )

        txt_path = await event.download_media()

        with open(txt_path, 'r', encoding='utf-8') as file:
            links = file.readlines()

        for link in links:

            url = link.strip()

            if url.startswith('http'):

                try:

                    await event.respond(
                        f"⬇️ Downloading:\n{url}"
                    )

                    # Delete old video
                    if os.path.exists("video.mp4"):
                        os.remove("video.mp4")

                    ydl_opts = {
                        'format': 'best[ext=mp4]',
                        'outtmpl': 'video.mp4',
                        'quiet': True,
                        'noplaylist': True
                    }

                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([url])

                    if os.path.exists("video.mp4"):

                        await event.client.send_file(
                            event.chat_id,
                            "video.mp4",
                            caption="✅ MP4 Video Ready"
                        )

                        os.remove("video.mp4")

                    else:

                        await event.respond(
                            "❌ Video Download नहीं हुई"
                        )

                except Exception as e:

                    await event.respond(
                        f"❌ Error:\n{str(e)}"
                    )

        os.remove(txt_path)

        await event.respond(
            "✅ सभी Links Process हो गए"
        )

# =========================
# Run Bot
# =========================

client.run_until_disconnected()
