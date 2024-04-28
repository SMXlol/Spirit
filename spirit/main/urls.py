from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include
from . import views

urlpatterns = [
    path('queue/', views.queue),
    path('faq/', views.faq),
    path('settings/', views.settings),
    path('names/', views.get_names),
    path('readmes/', views.get_readme),
    path('images/', views.get_image),
    path('fod/', views.all_fodder)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
