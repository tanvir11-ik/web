from django.shortcuts import render
from django.http import HttpResponse
from .models import admin




# Create your views here.

def home(request):
    return render(request,('home.html'))


def kobita(request):
    return render(request,('kobita.html'))

def contact(request):
    admin1 = admin()
    admin1.name = 'IH Masud'
    admin1.img = 'img.jpg'
    admin1.bdate = '12-Aug-1997'
    admin1.mobile = '01723457658'
    admin1.disc = 'kind man.'

    admin2 = admin()
    admin2.name = 'IH'
    admin2.img = 'img.jpg'
    admin2.bdate = '12-Aug-1997'
    admin2.mobile = '01723457658'
    admin2.disc = 'kind man.'

    admin3 = admin()
    admin3.name = 'Masud'
    admin3.img = 'img.jpg'
    admin3.bdate = '12-Aug-1997'
    admin3.mobile = '01723457658'
    admin3.disc = 'kind man.'

    admins = [admin1, admin2, admin3]

    return render(request, 'contact.html', {'admins': admins})


def menu(request):
    return render(request,('menu.html'))
