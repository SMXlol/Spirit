from django.shortcuts import render
from .models import Layout


def index(request):
    layout = Layout.objects.all()
    return render(request, 'layout/main.html', {'layout': layout})
