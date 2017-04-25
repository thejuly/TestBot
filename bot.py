from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

LINE_API = 'https://api.line.me/v2/bot/message/reply'
Authorization = '1sAimDh9L0wg5XAJeBYy96GrwzZFYQYAfTB+CrsdX5E/9gdt9oj5Lbc9NbRSHh5d05Ne9FDan12z6c9dbprv5TXRgjm4/+ioHTy6G91A2rNBiW999c0IlhsTcq5bfOyVf7OLRGtAAISIbHd84WemFgdB04t89/1O/w1cDnyilFU= ' #ENTER_ACCESS_TOKEN


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

'''
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))
'''

if __name__ == "__main__":
    app.run()    
