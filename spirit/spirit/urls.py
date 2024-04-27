from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from layout import views
from django.conf import settings
from layout import views

app_name = 'registration'

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),
    path('see-pet/', include('see_pet.urls')),
]
