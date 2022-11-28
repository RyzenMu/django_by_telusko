from django.urls import path 
from django.http import HttpResponse
from . import views

urlpatterns = [ 
    path('', views.index, name='Home Page'),
    path('index.html', views.listings, name='listings'),
    path('contact.html', views.contact, name='contact')
]