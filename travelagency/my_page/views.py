from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('Hello from My_Page')

def my_page_1(request):
    list = [1, 2, 3, 4, 5, 6]
    return render(request, 'my_page_1.html', {'list' : list})
