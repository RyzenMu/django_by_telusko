from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def first_page(request):
    return render(request, 'first_html_page.html')

def addition_page(request):
    number_1 = int(request.POST['number_1_html'])
    number_2 = int(request.POST['number_2_html'])
    result_python = number_1 + number_2
    return render(request, 'addition_html_page.html', {'result_html' : result_python, 'number_1': number_1,
        'number_2': number_2})
