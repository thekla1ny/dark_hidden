import discord
import asyncio
import requests
from io import BytesIO

TOKEN = input("Введи свой Discord токен: ")

CHANNEL_ID = 1380164920511041717
MESSAGE = """35к+
Много ивентов
Объединение на 300+
Копилка всегда полная
Также турниры проходят"""
IMAGE_URL = "https://github.com/thekla1ny/dark_hidden/raw/main/schb.jpg"

class MyClient(discord.Client):
    async def on_ready(self):
        print(f"✅ Авторизован как {self.user}")

        while True:
            try:
                # Загружаем картинку по ссылке
                response = requests.get(IMAGE_URL)
                img_bytes = BytesIO(response.content)

                channel = await self.fetch_channel(CHANNEL_ID)
                await channel.send(MESSAGE, file=discord.File(img_bytes, filename="image.jpg"))
                print("📤 Сообщение с картинкой отправлено.")
            except Exception as e:
                print(f"❌ Ошибка: {e}")

            await asyncio.sleep(7200)  # 7200 секунд = 2 часа

client = MyClient(intents=discord.Intents.default())
client.run(TOKEN, bot=False)
