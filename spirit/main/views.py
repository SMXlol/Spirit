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
    return HttpResponse(names)


def get_readme(request):
    pets = Pet.objects.all()
    names = []
    for i in pets:
        names.append(i.readme)
    return HttpResponse(names)


def get_image(request):
    pets = Pet.objects.all()
    names = []
    for i in pets:
        names.append(i.image_url)
    return HttpResponse(names)


def all_fodder(request):
    pets = Pet.objects.all()
    for pet in pets:
        if pet.name == "Мопс":
            pet.fodder += 100
        pet.save()
    print(pets.fodder)
    return HttpResponse(pets)


def all_balance(db, balance):
    for i in db['donation']:
        for j in i.keys():
            if j == "balance":
                i["balance"] += balance