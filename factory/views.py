from django.shortcuts import render 
from django.contrib.auth.models import User
# from django.contrib.sessions.models import Session
# from django.utils import timezone
# from django.contrib.auth.decorators import login_required


def index(request):
    context={"clase": "index"}
    return render(request, 'demo/index.html', context)


def laboratorio(request):
    context={"clase": "laboratorio"}
    return render(request, 'demo/laboratorio.html', context)