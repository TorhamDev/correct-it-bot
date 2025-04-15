import os
from dotenv import load_dotenv


from telethon import TelegramClient, events
from utils.wagner import spell_check
from utils.words import add_sentence_words, words


load_dotenv()

# Use your own values from my.telegram.org
api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")

client = TelegramClient(os.getenv("CLIENT_NAME"), api_id, api_hash)


@client.on(events.NewMessage(outgoing=True, pattern=r"(?i).*!fix"))
async def read(event):
    if event.is_reply:
        new = await event.get_reply_message()
        message = str()
        for word in new.raw_text.split():
            message += f"{spell_check(word, words)[0][0]} "

        await event.reply(message)


@client.on(events.NewMessage(outgoing=True, pattern=r"(?i).*!add"))
async def add_new_words(event):
    if event.is_reply:
        new = await event.get_reply_message()
        add_sentence_words(new.raw_text)
        await event.delete()


client.start()
client.run_until_disconnected()
