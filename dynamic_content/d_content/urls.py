from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.dynamic_content, name='dynamic_content')
]