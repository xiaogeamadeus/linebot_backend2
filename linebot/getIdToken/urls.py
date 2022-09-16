from django.urls import path

from . import views

urlpatterns = [
    path("login", views.login, name="index"),
    path("bot/others", views.others_bot, name="others_bot"),
    path("bot/available", views.available_bot, name="available_bot"),
    path("bot", views.root, name="root"),
    path("activate", views.activate, name="activate"),
    path("bot/<str:id>", views.id, name="show"),
]
