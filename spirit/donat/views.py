from django.shortcuts import render, redirect
from volunteer.models import *


def fodder(request, pet_name):
    pet = Pet.objects.get(name=pet_name)
    pet.fodder += 100
    pet.save()
    return redirect('/')


def balance(request, pet_name):
    pet = Pet.objects.get(name=pet_name)
    pet.balance += 100
    pet.save()
    return redirect('/')

