from django.shortcuts import render


def see_over(request):
    return render(request, 'volunteer/volunteer.html')
