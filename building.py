from tensorflow.keras.preprocessing.image import load_img, img_to_array
from flask import Flask, request, send_from_directory
from werkzeug.middleware.proxy_fix import ProxyFix
from linebot import LineBotApi, WebhookHandler
from linebot.models import *
# from linebot.v3.models import 
# from linebot.v3.webhook import WebhookHandler
# from linebot.v3.liff impor
# import tensorflow as tf
import json
# import cv2
# model = tf.keras.models.load_model('B3_2.h5')
channel_access = '5nUOSGO+Tz6kFzsLKrz6w2bA3sXULES/cKxcJvSF/ozbQSbMLF5++LdAx8hdDYPYEmoT8SVoQQezSN/uB5JWDb0tqc0cyOC9/OpAxO2entZyik1vHuav/MuQR6yyIHn52XRk2JMRY4JyQCj41sSjvgdB04t89/1O/w1cDnyilFU='
channel_secret = '9aaf935601935603e03695a94b247f2a'

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for =1 , x_host = 1 , x_proto = 1)
line_bot = LineBotApi(channel_access)
web_secret = WebhookHandler(channel_secret)

# @web_secret.add(MessageEvent, message=TextMessageContent)
# def line(event):
#     with ApiClient(line_bot_access) as api_client:
#         line_bot_api = MessagingApi(api_client)
#         line_bot_api.reply_message_with_http_info(
#             ReplyMessageRequest(
#                 reply_token=event.reply_token,
#                 messages=[TextMessage(text=event.message.text)]
#             )
#         )
@web_secret.add(MessageEvent, message=TextMessage)
def contact(event):
    text = event.message.text

    if text == 'ติดต่อ':
        bubble_strings =  """
        {
  "type": "template",
  "altText": "this is a carousel template",
  "template": {
    "type": "carousel",
    "columns": [
      {
        "thumbnailImageUrl": "https://cdn.discordapp.com/attachments/863787152965632022/1140596722649808906/image.png",
        "title": "คณะครุศาสตร์",
        "text": "ผลิตครูดี มีความรู้ เป็นผู้นำเทคนิควิธี มีศรัทธาในวิชาชีพครู",
        "actions": [
          {
            "type": "message",
            "label": "Phone",
            "text": "044-611221"
          }
        ],
        "imageBackgroundColor": "#FFFFFF"
      },
      {
        "thumbnailImageUrl": "https://media.discordapp.net/attachments/863787152965632022/1140596832326651915/image.png?width=698&height=465",
        "title": "คณะเทคโนโลยีอุตสาหกรรม",
        "text": "มุ่งผลิตบัณฑิตทางเทคโนโลยีอุตสาหกรรม เพื่อพัฒนาท้องถิ่น",
        "actions": [
          {
            "type": "message",
            "label": "Phone",
            "text": "044-611221"
          }
        ]
      },
      {
        "thumbnailImageUrl": "https://cdn.discordapp.com/attachments/863787152965632022/1140596878950539365/image.png",
        "title": "คณะเทคโนโลยีการเกษตร",
        "text": "เรียนรุ้ด้วยการปฏิบัติ ฝึกหัดสร้างประสบการณ์ สร้างงานเลี้ยงต",
        "actions": [
          {
            "type": "message",
            "label": "Phone",
            "text": "044-617426"
          }
        ]
      },
      {
        "thumbnailImageUrl": "https://cdn.discordapp.com/attachments/863787152965632022/1140596920084082778/image.png",
        "title": "คณะมนุษยศาสตร์และสังคมศาสตร์",
        "text": "สร้างคนด้วยศาสตร์ พัฒนาชาติด้วยภูมิปัญญา ธำรงศาสนาและวัฒนธรร",
        "actions": [
          {
            "type": "message",
            "label": "Phone",
            "text": "044-611389"
          }
        ]
      },
      {
        "thumbnailImageUrl": "https://cdn.discordapp.com/attachments/863787152965632022/1140596962543013938/image.png",
        "title": "คณะวิทยาศาสตร์",
        "text": "ผลิตบัณฑิตทางวิทยาศาสตร์และเทคโนโลยีมีความรู้คู่คุณธรรมเพื่อ",
        "actions": [
          {
            "type": "message",
            "label": "Phone",
            "text": "044-611221"
          }
        ]
      },
      {
        "thumbnailImageUrl": "https://cdn.discordapp.com/attachments/863787152965632022/1140597001843650670/image.png",
        "title": "คณะวิทยาการจัดการ",
        "text": "ความรู้ดี ทักษะเด่น เน้นคุณธรรม นำสังคม",
        "actions": [
          {
            "type": "message",
            "label": "Phone",
            "text": "044-611221"
          }
        ]
      },
      {
        "thumbnailImageUrl": "https://cdn.discordapp.com/attachments/863787152965632022/1140597047318286396/image.png",
        "title": "คณะพยาบาลศาสตร์",
        "text": "มุ่งผลิตบัณฑิตทางการพยาบาลที่มีคุณภาพ มีคุณธรรม นำสุขภาพสู่ป",
        "actions": [
          {
            "type": "message",
            "label": "Phone",
            "text": "044–611221"
          }
        ]
      }
    ]
  }
}
"""
        

        message = FlexSendMessage(alt_text="contact", contents=json.loads(bubble_strings))
        
        line_bot.reply_message(
                event.reply_token,
                message            
        )
@web_secret.add(MessageEvent, message = ImageMessage)
def predict_class(img):
    img = load_img(img, target_size = (300, 300))


if __name__ == '__main__':
    app.run(debug = False)
