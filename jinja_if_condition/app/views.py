from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('Hello Jinja If Condition')

def jinja(request):
    rang = []
    for i in range(10):
        rang.append(i)

    
    my_value =[]
    for i in rang:
        if i%2 == 0:
            my_value.append(1)
        else:
            my_value.append(0)
    return render(request, 'index.html', {'rang': rang, 'value' : my_value})
