from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from volunteer.models import *


def index(request):
    return render(request, 'main/main.html')


def queue(request):
    return render(request, 'main/queue.html')


def faq(request):
    return render(request, 'main/faq.html')


def settings(request):
    return render(request, 'main/settings.html')


def get_names(request):
    pets = Pet.objects.all()
    names = []
    for i in pets:
        names.append(i.name)
    return names

