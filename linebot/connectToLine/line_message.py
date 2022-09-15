import json
import ssl
import urllib.request

import environ
from getIdToken.models import Activation, Bot

from .utils import message_creater

ssl._create_default_https_context = ssl._create_unverified_context

env = environ.Env()


reply_endpoint_URL = "https://api.line.me/v2/bot/message/reply"
accessToken = env("LINE_CHANNEL_ACCESS_TOKEN")
header = {"Content-Type": "application/json", "Authorization": "Bearer " + accessToken}

interpreter_endpoint_URL = env("INTERPRETER_ENDPOINT_URL")


class lineMessage:
    def __init__(self, messages):
        self.messages = messages

    def reply(self, reply_token, user_id):
        activation = Activation.objects.get(user_id=user_id)
        bot = Bot.objects.get(bot_id=activation.bot_id)

        data = {
            "message": self.messages[0]["text"],
            "flowchart": bot.flowchart,
        }

        req = urllib.request.Request(
            interpreter_endpoint_URL,
            data=json.dumps(data).encode(),
            headers={"Content-Type": "application/json"},
        )

        with urllib.request.urlopen(req) as response:
            res = response.read().decode(response.headers.get_content_charset())
            res_json = json.loads(res)
            reply = res_json["reply"]

            body = {
                "replyToken": reply_token,
                "messages": message_creater.create_single_message(reply),
            }
            req = urllib.request.Request(
                reply_endpoint_URL, json.dumps(body).encode(), header
            )
            try:
                with urllib.request.urlopen(req) as res:
                    body = res.read()
            except urllib.error.HTTPError as err:
                print("エラー1")
                print(err)
            except urllib.error.URLError as err:
                print("エラー2")
                print(err.reason)
