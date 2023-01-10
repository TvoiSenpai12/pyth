from telethon import TelegramClient, events
# Тут вставляй свои данные с https://my.telegram.org/apps
api_id = '16851554'
api_hash = '46e14bf8998f41ca3d889bcf430d4cef'

client = TelegramClient('anoni', api_id, api_hash)
client.start()

@client.on(events.NewMessage(-1001708158788))

async def main(event):
    await client.forward_messages(-1001771993154, event.message)
    
client.run_until_disconnected()