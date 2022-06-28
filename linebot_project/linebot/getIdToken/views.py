from django.shortcuts import render
from django.http import HttpResponse
import json
# from .models import User
# from .models import Restaurant
from django.db.models import Q
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the getIdToken index.")