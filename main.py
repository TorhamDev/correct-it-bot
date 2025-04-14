import os
from dotenv import load_dotenv


from telethon import TelegramClient, events
from utils.wagner_fischer import spell_check


load_dotenv()

# Use your own values from my.telegram.org
api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")

client = TelegramClient(os.getenv("CLIENT_NAME"), api_id, api_hash)


@client.on(events.NewMessage(outgoing=True, pattern=r"(?i).*!check"))
async def read(event):
    print(event.is_reply)
    if event.is_reply:
        new = await event.get_reply_message()
        message = str()
        results = spell_check(new.raw_text)
        for r in results:
            message += f"{r}\n"

        await event.reply(message)


client.start()
client.run_until_disconnected()
