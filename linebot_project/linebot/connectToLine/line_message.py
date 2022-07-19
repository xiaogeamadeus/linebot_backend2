import urllib.request
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json


reply_endpoint_URL = "https://api.line.me/v2/bot/message/reply"
accessToken = "XVwj5RzYQoB6a0c8423Xv2lDoxbmGEctHar5XObxGIKHV54xgmuuKUZx09eya+aujZ8/06WpI5PABJ9wP/UpgMKaxNoYZ/OZevpOGI6Vs3MOqyxiyuEO/0q1tEhUWJs4r089fDpC3NGAhzgGgwbAgwdB04t89/1O/w1cDnyilFU="
header = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + accessToken
}


# {
#   type:"text",
#   text:"hogehoge"
# }
# the structure of respond

class lineMessage():
    def __init__(self, messages):
        self.messages = messages

    def reply(self, reply_token):
        body = {
            'replyToken': reply_token,
            'messages': self.messages
        }
        print(body)
        req = urllib.request.Request(reply_endpoint_URL, json.dumps(body).encode(), header)
        try:
            with urllib.request.urlopen(req) as res:
                body = res.read()
        except urllib.error.HTTPError as err:
            print(err)
        except urllib.error.URLError as err:
            print(err.reason)
