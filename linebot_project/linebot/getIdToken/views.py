from django.shortcuts import render
from django.http import HttpResponse
import json
# from .models import User
# from .models import Restaurant
from django.db.models import Q
# Create your views here.

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