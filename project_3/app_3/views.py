from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('Hello Django from Project_3 for second time')

def page1(request):
    return HttpResponse('Page 1 posted now')

def page2(request):
    return HttpResponse('Page 2 posted now from django')
