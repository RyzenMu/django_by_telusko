from django.urls import path 

from . import  views  

urlpatterns = [ 
    path('44', views.home, name='home')
]