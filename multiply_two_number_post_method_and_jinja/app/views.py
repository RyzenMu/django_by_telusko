from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'index.html')

def multiply(request):
    number_1 = int(request.GET['number_1'])
    number_2 = int(request.GET['number_2'])
    result = number_1 * number_2
    return render(request, 'multiply.html', {'result': result})
