from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello world from project 2')

# Create your views here.
