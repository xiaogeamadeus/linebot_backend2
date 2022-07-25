from django.urls import path
from . import views

urlpatterns = [
    path('login', views.index, name='index'),
    path('bot', views.root, name='root'),
    path('activate', views.activate, name='activate'),
    path('bot/<str:id>', views.id, name='show'),
]