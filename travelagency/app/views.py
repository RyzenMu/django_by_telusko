from django.shortcuts import render
from django.http import HttpResponse
from .models import Destinations

# Create your views here.

def home(request):
    loaction_1 = 'Mumbai'
    location_2 = 'Goa'

    dest1 = Destinations()
    dest1.name = 'mumbai'
    dest1.price = 700

    dest2 = Destinations()
    dest2.name = 'Goa'
    dest2.price = 800


    # return render(request, 'index.html', {'location_1': loaction_1, 'location_2' : location_2,
    # 'price_1' : 700, 'price_2' : 800})

def forloop(request):
    names = ['apple', 'banana', 'carrot']
    return render(request, 'forloop.html', {'names' : names})
