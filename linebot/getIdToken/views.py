import json
from datetime import datetime

import requests
from django.core import serializers
from django.db.models import Q
from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status

from .auth import verify_user
from .models import Activation, Bot, User
from .serializer import BotSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the getIdToken index.")


def getIdToken(request):
    if request.method == "POST":
        if request.POST:
            idToken = request.POST.get("idToken", 0)
            return HttpResponse("Good!")
        else:
            return HttpResponse("ERROR: It is a wrong input.")


def others_bot(request):
    if request.method == "GET":
        user = verify_user(request)
        if user is None:
            return HttpResponse("Auth failed", status=403)
        bots = Bot.objects.filter(is_public=True).order_by("-updated_at")
        serializer = BotSerializer(bots, many=True)
        return HttpResponse(json.dumps(serializer.data))

    return HttpResponse("Only GET requests are allowed")


def root(request):
    if request.method == "GET":
        user = verify_user(request)
        if user is None:
            return HttpResponse("Auth failed", status=403)
        bots = Bot.objects.filter(created_by=user.user_id).order_by("-updated_at")
        serializer = BotSerializer(bots, many=True)
        return HttpResponse(json.dumps(serializer.data))
    elif request.method == "POST":
        return create(request)

    return HttpResponse("Only GET and POST requests are allowed")


def id(request, id):
    if request.method == "GET":
        bot = Bot.objects.get(bot_id=id)

        if not bot.is_public:
            user = verify_user(request)
            if user is None:
                return HttpResponse("Unauthorized", status=401)
            if user.user_id != bot.created_by.user_id:
                return HttpResponse("Forbidden", status=403)

        serializer = BotSerializer(bot)

        return HttpResponse(json.dumps(serializer.data))
    elif request.method == "DELETE":
        return delete(request, id)
    elif request.method == "PUT":
        return update(request, id)

    return HttpResponse("Only GET and DELETE requests are allowed")


def login(request):
    if request.method == "POST":
        user = verify_user(request)
        if user is None:
            return HttpResponse("Auth failed", status=403)

        user_dict = model_to_dict(user)
        return HttpResponse(json.dumps(user_dict))

    return HttpResponse("Only POST requests are allowed")


def create(request):
    if request.method != "POST":
        return HttpResponse("Only POST requests are allowed")

    body = json.loads(request.body)
    user = verify_user(request)
    if user is None:
        return HttpResponse("Auth failed", status=403)

    bot = Bot(
        bot_id=body["bot_id"],
        name=body["name"],
        created_by=user,
        flowchart=body["flowchart"],
        is_public=False,
    )

    bot.save()
    bot_dict = model_to_dict(bot)

    return HttpResponse(json.dumps(bot_dict))


def delete(request, id):
    if request.method != "DELETE":
        return HttpResponse("Only DELETE requests are allowed")

    user = verify_user(user)

    if user is None:
        return HttpResponse("Unauthorized", status=401)

    bot = Bot.objects.get(bot_id=id)

    if bot.created_by.user_id != user.id:
        return HttpResponse("Forbidden", status=403)

    bot.delete()
    return HttpResponse("Bot deleted")


def update(request, id):
    if request.method != "PUT":
        return HttpResponse("Only PUT requests are allowed")

    body = json.loads(request.body)

    user = verify_user(request)
    if user is None:
        return HttpResponse("Auth failed", status=403)
    bot = Bot.objects.get(bot_id=id)

    if "name" in body:
        bot.name = body["name"]

    if "created_by" in body:
        bot.created_by = user

    if "flowchart" in body:
        bot.flowchart = body["flowchart"]

    if "is_public" in body:
        bot.is_public = body["is_public"]

    bot.save()
    bot_dict = model_to_dict(bot)

    return HttpResponse(json.dumps(bot_dict))


def activate(request):
    if request.method != "POST":
        return HttpResponse("Only DELETE requests are allowed")

    body = json.loads(request.body)

    _, created = Activation.objects.update_or_create(
        user_id=body["user_id"],
        defaults={
            "bot_id": body["bot_id"],
        },
    )

    if created:
        return HttpResponse("Activated")
    else:
        return HttpResponse("Activated", status=status.HTTP_409_CONFLICT)
