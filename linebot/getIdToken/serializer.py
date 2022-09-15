from dataclasses import fields

from pyexpat import model
from rest_framework import serializers

from .models import Bot, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class BotSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Bot

        fields = (
            "bot_id",
            "name",
            "flowchart",
            "is_public",
            "created_at",
            "updated_at",
            "created_by",
        )
