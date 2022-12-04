from django.shortcuts import render
from .models import Destinations

# Create your views here.

def home(request):
    dest1 = Destinations()
    dest1.name = "Delhi"
    dest1.price = 1000
    dest1.image = 'delhi.jpg'
    return render(request, 'index.html', {'dest1' : dest1})
