from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('Project_2 Started.......')


def ren(request):
    return render(request, 'ren.html')