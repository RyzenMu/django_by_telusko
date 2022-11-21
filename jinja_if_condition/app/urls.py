from django.urls import path 
from . import views

urlpatterns = [ 
    path('', views.home, name='home'),
    path('jinja', views.jinja, name='jinja')
]