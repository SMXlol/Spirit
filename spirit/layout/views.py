from django.shortcuts import render, redirect
from .models import Names
from volunteer.models import *



def index(request):
    pets = Pet.objects.all()
    names = []
    title = []
    img = []
    numbers = []
    for i in pets:
        names.append(i.name)
    for i in range(len(names)):
        numbers.append(i)
    for i in pets:
        title.append(i.readme)
    for i in pets:
        img.append(i.image_url)
    context = {'name_1': names[0], 'name_2': names[1], 'name_3': names[2], 'title_1': title[0], 'title_2': title[1],  'title_3': title[2], 'img_1': img[0], 'img_2': img[1], 'img_3': img[2]}
    print(context)
    return render(request, 'layout/main.html', context)

