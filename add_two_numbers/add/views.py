from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return HttpResponse('Hello World')


def add(request):
    number_1 = int(request.GET["num_1"])
    number_2 = int(request.GET["num_2"])
    total = number_1 + number_2
    return render(request, ('index.html'), {'total' : total})

def result(request):
    return render(request, ('result.html'))


