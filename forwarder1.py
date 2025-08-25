import requests
import time

# Твой user токен (⚠️ осторожно, палить его нельзя)
TOKEN = input("Нелегальная реклама Shichibukai. Введи свой discord токен: ").strip()

# ID канала, куда отправлять
CHANNEL_ID = "1380164920511041717"

# Сообщение
MESSAGE = """35к+
Много ивентов
Объединение на 300+
Копилка всегда полная
Также турниры проходят"""

# Ссылка на картинку (она должна быть доступна публично)
IMAGE_URL = "https://raw.githubusercontent.com/thekla1ny/dark_hidden/main/schb.jpg?raw=true"

# API Discord
url = f"https://discord.com/api/v9/channels/{CHANNEL_ID}/messages"
headers = {
    "Authorization": TOKEN,
    "Content-Type": "application/json"
}

def send_message():
    payload = {
        "content": MESSAGE,
        "embeds": [
            {
                "image": {"url": IMAGE_URL}
            }
        ]
    }
    r = requests.post(url, headers=headers, json=payload)
    if r.status_code == 200:
        print("✅ Сообщение отправлено")
    else:
        print(f"❌ Ошибка: {r.status_code} | {r.text}")

def main():
    while True:
        send_message()
        print("⏳ Жду 2 часа...")
        time.sleep(7200)  # 2 часа

if __name__ == "__main__":
    main()

