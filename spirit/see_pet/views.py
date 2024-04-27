from django.shortcuts import render


def see_over(request):
    return render(request, 'see_pet/see_pet.html')
