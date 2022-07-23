import json
import environ
import os
import ssl
import urllib.request
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import message_creater
from getIdToken.models import Activation, Bot

ssl._create_default_https_context = ssl._create_unverified_context

env = environ.Env()


reply_endpoint_URL = "https://api.line.me/v2/bot/message/reply"
accessToken = "XVwj5RzYQoB6a0c8423Xv2lDoxbmGEctHar5XObxGIKHV54xgmuuKUZx09eya+aujZ8/06WpI5PABJ9wP/UpgMKaxNoYZ/OZevpOGI6Vs3MOqyxiyuEO/0q1tEhUWJs4r089fDpC3NGAhzgGgwbAgwdB04t89/1O/w1cDnyilFU="
header = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + accessToken
}

interpreter_endpoint_URL = env('INTERPRETER_ENDPOINT_URL')


# {
#   type:"text",
#   text:"hogehoge"
# }
# the structure of respond

class lineMessage():
    def __init__(self, messages):
        self.messages = messages

    def reply(self, reply_token, user_id):
        activation = Activation.objects.get(user_id=user_id)
        bot = Bot.objects.get(bot_id=activation.bot_id)


        data = {
            'message': self.messages[0]['text'],
            # 'flowchart': bot.flowChart,
            # ↓ テスト用
            'flowchart': '[{\"id\":\"5\",\"node\":{\"id\":\"5\",\"node\":{\"label\":\"テキスト入力\",\"color\":\"#06c755\",\"nodeType\":\"textInputNode\"},\"pos\":{\"x\":450,\"y\":107},\"inPoints\":[],\"outPoints\":[{\"type\":\"number\",\"label\":\"confirmed\",\"limit\":null}],\"createrInputValue\":\"\",\"isInitialNode\":false,\"type\":\"textInputNode\"},\"outputs\":[\"6\"]},{\"id\":\"6\",\"node\":{\"id\":\"6\",\"node\":{\"label\":\"テキスト含有\",\"color\":\"#a9a9a9\",\"nodeType\":\"includeCheckNode\"},\"pos\":{\"x\":548,\"y\":296},\"inPoints\":[{\"type\":\"number\",\"label\":\"\",\"limit\":null}],\"outPoints\":[{\"type\":\"number\",\"label\":\"yes\",\"limit\":null},{\"type\":\"number\",\"label\":\"no\",\"limit\":null}],\"createrInputValue\":\"hello\",\"isInitialNode\":false,\"type\":\"includeCheckNode\"},\"outputs\":[\"8\",\"12\"]},{\"id\":\"8\",\"node\":{\"id\":\"8\",\"node\":{\"label\":\"テキスト出力\",\"color\":\"#06c755\",\"nodeType\":\"textOutputNode\"},\"pos\":{\"x\":428,\"y\":475},\"inPoints\":[{\"type\":\"number\",\"label\":\"\",\"limit\":null}],\"outPoints\":[],\"createrInputValue\":\"こんにちは\",\"isInitialNode\":false,\"type\":\"textOutputNode\"},\"outputs\":[]},{\"id\":\"12\",\"node\":{\"id\":\"12\",\"node\":{\"label\":\"テキスト出力\",\"color\":\"#06c755\",\"nodeType\":\"textOutputNode\"},\"pos\":{\"x\":691,\"y\":468},\"inPoints\":[{\"type\":\"number\",\"label\":\"\",\"limit\":null}],\"outPoints\":[],\"createrInputValue\":\"さようなら\",\"isInitialNode\":false,\"type\":\"textOutputNode\"},\"outputs\":[]}]'
        }

        req = urllib.request.Request(interpreter_endpoint_URL, data=json.dumps(data).encode(), headers={"Content-Type" : "application/json"})

        with urllib.request.urlopen(req) as response:
            res = response.read().decode(response.headers.get_content_charset())
            res_json = json.loads(res)
            reply = res_json['reply']
        
            body = {
                'replyToken': reply_token,
                'messages': message_creater.create_single_text_message(reply)
            }
            print(body)
            req = urllib.request.Request(reply_endpoint_URL, json.dumps(body).encode(), header)
            try:
                with urllib.request.urlopen(req) as res:
                    body = res.read()
            except urllib.error.HTTPError as err:
                print("エラー1")
                print(err)
            except urllib.error.URLError as err:
                print("エラー2")
                print(err.reason)
