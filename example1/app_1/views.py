from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#Http Response
def home(request):
    return HttpResponse('This is HTTP response')


#Page Render
def page_1(request):
    return render(request, 'page_1.html')


#Page Render with dynamic variable
def page_2(request):
    return render(request, 'page_2.html', {'name' : "muruganantham", 'city' : 'chennai'})


def page_3(request):
    return render(request, 'page_2.html', {'name' : 'divya', 'city': 'trichy'})


