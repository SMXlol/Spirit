from django.shortcuts import render
from .models import Names


def index(request):
    name = Names.name
    return render(request, 'layout/main.html', {'layout': name})

