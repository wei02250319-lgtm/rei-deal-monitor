import os
import requests
from bs4 import BeautifulSoup

BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

BRANDS = ["Patagonia", "Arc'teryx"]
DISCOUNT_THRESHOLD = 30


def send_telegram(message):
    if not BOT_TOKEN or not CHAT_ID:
        print("未找到 Telegram 配置")
        return

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message,
        "disable_web_page_preview": False,
    }

    response = requests.post(url, data=data, timeout=20)
    response.raise_for_status()
    print("Telegram 通知发送成功")


def test_telegram():
    message = (
        "🛒 REI 折扣监控已启动\n\n"
        "监控品牌：Patagonia、Arc'teryx\n"
        "折扣条件：30% OFF 及以上\n"
        "检查频率：每15分钟\n\n"
        "✅ GitHub Actions 云端运行正常"
    )

    send_telegram(message)


if __name__ == "__main__":
    print("REI 折扣监控程序启动")
    test_telegram()
