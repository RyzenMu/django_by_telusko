from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_page(request):
    return render(request, 'index.html')

def makemytrip(request):
    return render(request, 'makemytrip.html')

def kaveri(request):
    return render(request, 'home_page.html')
