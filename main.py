from telethon import TelegramClient, events
import yt_dlp
import os
import glob

# =========================
# TELEGRAM API DETAILS
# =========================

API_ID = 31911187

API_HASH = "8291ae3d580f1fb5f8f84e0e3c6a3e6f"

BOT_TOKEN = "8908901463:AAHuKRv0wbGys3TOHNO7tElnv8Gl75G6cRk"

# =========================
# START BOT
# =========================

client = TelegramClient(
    'bot',
    API_ID,
    API_HASH
).start(bot_token=BOT_TOKEN)

print("✅ BOT STARTED SUCCESSFULLY")

# =========================
# TXT FILE HANDLER
# =========================

@client.on(events.NewMessage)

async def txt_handler(event):

    # Check TXT file
    if event.message.file and event.message.file.name.endswith('.txt'):

        await event.respond(
            "✅ TXT FILE मिल गई\n🎬 VIDEO DOWNLOAD START..."
        )

        # Download TXT
        txt_path = await event.download_media()

        # Read TXT
        with open(txt_path, 'r', encoding='utf-8') as file:
            links = file.readlines()

        # Process every link
        for link in links:

            url = link.strip()

            # Check valid URL
            if url.startswith("http"):

                try:

                    await event.respond(
                        f"⬇️ DOWNLOADING:\n{url}"
                    )

                    # Delete old videos
                    old_files = glob.glob("*.mp4")

                    for old in old_files:
                        os.remove(old)

                    # yt-dlp options
                    ydl_opts = {
                        'format': 'bestvideo+bestaudio/best',
                        'merge_output_format': 'mp4',
                        'outtmpl': '%(title)s.%(ext)s',
                        'quiet': False,
                        'noplaylist': True
                    }

                    # Download video
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([url])

                    # Find MP4 file
                    mp4_files = glob.glob("*.mp4")

                    if mp4_files:

                        for video in mp4_files:

                            await event.client.send_file(
                                event.chat_id,
                                video,
                                caption="✅ MP4 VIDEO READY"
                            )

                            os.remove(video)

                    else:

                        await event.respond(
                            "❌ MP4 VIDEO नहीं मिली"
                        )

                except Exception as e:

                    await event.respond(
                        f"❌ ERROR:\n{str(e)}"
                    )

        # Delete TXT
        os.remove(txt_path)

        await event.respond(
            "✅ सभी LINKS PROCESS हो गए"
        )

# =========================
# RUN BOT
# =========================

client.run_until_disconnected()
