from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('Hello Jinja')

def jinja(request):
    cars = ['maruthi', 
            'honda',
            'tata',
            'skoda']
    
    rang = []
    for i in range(10):
        rang.append(i)

    

    return render(request, 'index.html', {'cars': cars, 'rang' : rang})
