from django.shortcuts import render
from django.http import HttpResponse

# Create your views here

def home(request):
    return HttpResponse(' Subtracting Two Numbers from two variables')

def sub(request):
    number_1 = int(request.GET["number_1"])
    number_2 = int(request.GET["number_2"])
    total = number_1 - number_2
    return render(request, 'index.html', {'total': total})