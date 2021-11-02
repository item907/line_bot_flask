from flask import Flask
app = Flask(__name__)

from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

line_bot_api = LineBotApi('RRi4eJ038fJxCduMoN6JQ4AQiPLFktaGN56dhMMxSLgQ6tkafwMU6fx8Hnv4ARqv9WfWa9ktjhhGPS0sjZX/KMFG0VwzKWsnrWNMuov1ZaOwrK8p5KT85d2qCRo5c0hnKYthPZGyubv62xSbEfozKAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('d6e181b5ad08d0522319b6318e979e32')

@app.route("/callback", methods = ['POST'])
def callback():
	signature = request.headers['X-Line-Signature']
	body = request.get_data(as_text = True)
	try:
		handler.handle(body, signature)
	except InvalidSignatureError:
		abort(400)
	return 'OK'
	
@handler.add(MessageEvent, message = TextMessage)
def handle_message(event):
	line_bot_api.reply_message(event.reply_token, TextSendMessage(text = event.message.text))
	
if __name__ == '__main__':
	app.run()