from django.urls import path
from . import views

urlpatterns = [
    path('login', views.index, name='index'),
    path('bot', views.root, name='root'),
    path('bot/<str:id>', views.id, name='show'),
    path('bot/activate', views.activate),
]