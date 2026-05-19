@client.on(events.NewMessage(func=lambda e: e.file))
async def file_handler(event):
    # बोट यहाँ फाइल डाउनलोड करेगा
    path = await event.download_media()
    await event.respond(f"फाइल डाउनलोड हो गई: {path}")

    # अगर फाइल .txt है, तो उसे पढ़कर लिंक निकालेगा
    if path.endswith('.txt'):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
            # यहाँ आप लिंक सर्च करने का लॉजिक जोड़ सकते हैं
            await event.respond("मैंने फाइल पढ़ ली है, लिंक नीचे हैं:")
