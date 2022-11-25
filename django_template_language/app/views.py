from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def page0(request):
    name = 'This is Page 0'
    return render(request, 'page0.html', {'var': name})

def page1(request):
    name = 'This is Page 1'
    return render(request, 'page1.html', {'var': name})

def page2(request):
    name = 'This is Page 2'
    return render(request, 'page2.html', {'var': name})

