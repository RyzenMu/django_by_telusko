from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def input(request):
    result = render(request, 'input.html')
    return HttpResponse(result)

def action(request):
    number_1 = int(request.POST['number_1'])
    number_2 = int(request.POST['number_2'])
    answer = number_1-number_2
    answer = render(request, 'answer.html', {'answer': answer})
    return HttpResponse(answer)
