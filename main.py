@client.on(events.NewMessage)
async def debug_handler(event):
    if event.message.file and event.message.file.name.endswith('.txt'):
        path = await event.download_media()
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read(500) # सिर्फ शुरुआती 500 अक्षर
            await event.respond(f"फाइल के अंदर यह लिखा है:\n\n{content}")
