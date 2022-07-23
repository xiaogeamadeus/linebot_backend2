# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
# import utils.message_creater as mc
from .utils import message_creater
from .line_message import lineMessage

import base64
import hashlib
import hmac



# # define the function
# def add_args(a, b):
#     return a + b
#
#
# def check(secret_key):
#     channel_secret = 'd79a825ec7d0940a59ac9507ad75cac7'  # Channel secret string
#     body = secret_key  # Request body string
#     hash = hmac.new(channel_secret.encode('utf-8'),
#                     body.encode('utf-8'), hashlib.sha256).digest()
#     signature = base64.b64encode(hash)
#
#     return True
    # Compare x-line-signature request header and the signature

# Access function
@csrf_exempt
def messagePost(request):
    if request.method == 'POST':
        request = json.loads(request.body.decode('utf-8'))
        events = request['events']
        for event in events:
            message = event['message']
            reply_token = event['replyToken']
            user_id = event['source']['userId']
            line_message = lineMessage(message_creater.create_single_text_message(message['text']))
            line_message.reply(reply_token, user_id)
        return HttpResponse("ok")
