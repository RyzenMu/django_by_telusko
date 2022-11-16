from django.shortcuts import render

# Create your views here.

def dynamic_content(request):
    return render(request, 'index.html', {'name': 'muruga', 'age' : 40, 'gender' : 'male'})
