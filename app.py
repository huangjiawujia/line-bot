from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = "這裡先不要動"

@app.route("/webhook", methods=['POST'])
def webhook():
    data = request.json

    for event in data['events']:
        if event['type'] == 'message':
            msg = event['message']['text']
            reply_token = event['replyToken']

            if "價格" in msg:
                reply(reply_token, "我們的價格是100元")
            elif "時間" in msg:
                reply(reply_token, "營業時間是9:00~18:00")

    return "OK"

def reply(token, text):
    url = "https://api.line.me/v2/bot/message/reply"
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "replyToken": token,
        "messages": [{"type": "text", "text": text}]
    }
    requests.post(url, headers=headers, json=data)
