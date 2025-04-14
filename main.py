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
        for word in new.raw_text.split():
            print(spell_check(word))
            print("------------------")
            message += f"{spell_check(word)[0][0]} "

        await event.reply(message)


client.start()
client.run_until_disconnected()
