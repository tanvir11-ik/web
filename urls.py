from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=''),
    path('kobita', views.kobita, name='kobita'),
    path('contact', views.contact, name='contact'),
    path('menu', views.menu, name='menu'),
]