from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    loaction_1 = 'Mumbai'
    location_2 = 'Goa'
    return render(request, 'index.html', {'location_1': loaction_1, 'location_2' : location_2})