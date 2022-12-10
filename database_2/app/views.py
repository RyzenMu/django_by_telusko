from django.shortcuts import render

# Create your views here.

from .models import Bikes

platina = Bikes()

platina.name = 'Platina'
platina.capacity = 100
platina.price = 65000
platina.description = ' Low Budget Bike for Starters'
platina.cooling = 'air cooling'
