from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include
from . import views

urlpatterns = [
    path('fodder/<str:pet_name>/', views.fodder),
    path('balance/<str:pet_name>/', views.balance),
]
