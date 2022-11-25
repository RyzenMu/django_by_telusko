from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.home),
    path('add', views.add, name='add'),
    path('pathaddition', views.addition, name='addition')
]