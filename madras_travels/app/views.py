from django.shortcuts import render
from .models import Destination

# Create your views here.

def home(request):

    dest1 = Destination()
    dest1.name = 'Delhi'
    dest1.price = 1000
    dest1.image = 'delhi.jpg'

    dest2 = Destination()
    dest2.name = 'Mumbai'
    dest2.price = 900
    dest2.image = 'mumbai.jpg'

    dest3 = Destination()
    dest3.name = 'Kolkata'
    dest3.price = 800
    dest3.image = 'kolkata.jpeg'

    dests = [dest1, dest2, dest3]


    return render(request, 'index.html', {'dests': dests})
