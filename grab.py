from telethon import TelegramClient, events
# Тут вставляй свои данные с https://my.telegram.org/apps
api_id = '16851554'
api_hash = '46e14bf8998f41ca3d889bcf430d4cef'

client = TelegramClient('anon', api_id, api_hash)
client.start()