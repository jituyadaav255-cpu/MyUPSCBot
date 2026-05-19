from telethon import TelegramClient, events
import yt_dlp
import os

# =========================
# Telegram API Details
# =========================

API_ID = 31911187

API_HASH = "8291ae3d580f1fb5f8f84e0e3c6a3e6f"

BOT_TOKEN = "8908901463:AAHuKRv0wbGys3TOHNO7tElnv8Gl75G6cRk"

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

    # TXT file check
    if event.message.file and event.message.file.name.endswith('.txt'):

        await event.respond(
            "✅ TXT File मिल गई\n🎬 Video Download शुरू..."
        )

        # Download TXT
        txt_path = await event.download_media()

        # Read TXT
        with open(txt_path, 'r', encoding='utf-8') as file:
            links = file.readlines()

        # Process Every Link
        for link in links:

            url = link.strip()

            # Valid URL Check
            if url.startswith("http"):

                try:

                    await event.respond(
                        f"⬇️ Downloading:\n{url}"
                    )

                    # Delete old files
                    for f in os.listdir():
                        if f.endswith(".mp4"):
                            os.remove(f)

                    # Download Settings
                    ydl_opts = {
                        'format': 'bestvideo+bestaudio/best',
                        'merge_output_format': 'mp4',
                        'outtmpl': 'video.%(ext)s',
                        'quiet': False,
                        'noplaylist': True
                    }

                    # Download Video
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([url])

                    # Find MP4 File
                    sent = False

                    for file in os.listdir():

                        if file.endswith(".mp4"):

                            await event.client.send_file(
                                event.chat_id,
                                file,
                                caption="✅ MP4 Video Ready"
                            )

                            os.remove(file)

                            sent = True

                    if not sent:

                        await event.respond(
                            "❌ MP4 Video नहीं मिली"
                        )

                except Exception as e:

                    await event.respond(
                        f"❌ Error:\n{str(e)}"
                    )

        # Delete TXT
        os.remove(txt_path)

        await event.respond(
            "✅ सभी Links Process हो गए"
        )

# =========================
# Run Bot
# =========================

client.run_until_disconnected()
