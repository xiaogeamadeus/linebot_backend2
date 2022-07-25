from rest_framework import status
from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Bot
from .models import Activation
from django.db.models import Q
from datetime import datetime
from django.core import serializers
from django.forms.models import model_to_dict

def index(request):
    return HttpResponse("Hello, world. You're at the getIdToken index.")

def getIdToken(request):
    #/login/getIdToken?
    if request.method == 'POST':
        if request.POST:
            idToken = request.POST.get('idToken', 0)
            return HttpResponse('Good!')
        else:
            return HttpResponse('ERROR: It is a wrong input.')

def root(request):
    developerId = request.GET.get('developerId')
    print(developerId)
    if request.method == 'GET':
        return index(request, developerId)
    elif request.method == 'POST':
        return create(request)

    return HttpResponse('Only GET and POST requests are allowed')

def id(request, id):
    if request.method == 'GET':
        return show(request, id)
    elif request.method == 'DELETE':
        return delete(request, id)
    elif request.method == 'PUT':
        return update(request, id)

    return HttpResponse('Only GET and DELETE requests are allowed')

def index(request, developerId):
    bots = Bot.objects.filter(developerId = developerId)

    return HttpResponse(serializers.serialize('json', bots))

def show(request, id):
    bot = Bot.objects.get(bot_id=id)
    bot_dict = model_to_dict(bot)

    return HttpResponse(json.dumps(bot_dict))
    

def create(request):
    if request.method != 'POST':
        return HttpResponse('Only POST requests are allowed')

    body = json.loads(request.body)

    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    bot = Bot(
        bot_id=body['bot_id'],
        name=body['name'],
        developerId=body['developerId'],
        flowChart=body['flowChart'],
        createdAt=now,
        updateAt=now
    )

    bot.save()
    bot_dict = model_to_dict(bot)

    return HttpResponse(json.dumps(bot_dict))

def delete(request, id):
    if request.method != 'DELETE':
        return HttpResponse('Only DELETE requests are allowed')

    bot = Bot.objects.get(bot_id=id)
    bot.delete()
    return HttpResponse('Bot deleted')

def update(request, id):
    if request.method != 'PUT':
        return HttpResponse('Only PUT requests are allowed')
    
    bot = Bot.objects.get(bot_id=id)
    
    body = json.loads(request.body)
    
    if "name" in body:
        bot.name=body['name']

    if "developerId" in body:
        bot.developerId=body['developerId']

    if "flowChart" in body:
        bot.flowChart=body['flowChart']

    bot.updateAt=datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    bot.save()
    bot_dict = model_to_dict(bot)

    return HttpResponse(json.dumps(bot_dict))

def activate(request):
    if request.method != 'POST':
        return HttpResponse('Only DELETE requests are allowed')

    body = json.loads(request.body)

    _, created = Activation.objects.update_or_create(
      bot_id=body['bot_id'],
      user_id=body['user_id'],
      defaults={}
    )

    if created:
      return HttpResponse("Activated")
    else:
      return HttpResponse("Activated", status=status.HTTP_409_CONFLICT)