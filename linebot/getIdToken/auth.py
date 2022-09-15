import requests
from django.http import HttpResponse

from .models import Activation, Bot, User


def verify_user(request):
    id_token = request.headers.get("Authorization")

    if id_token is None:
        return None

    response = requests.post(
        "https://api.line.me/oauth2/v2.1/verify",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data={"id_token": id_token, "client_id": "1657383189"},
    ).json()

    if "error" in response.keys() is not None:
        print(id_token, response)
        return None

    user, created = User.objects.update_or_create(
        user_id=response["sub"],
        name=response["name"],
        picture=response["picture"],
    )

    return user
