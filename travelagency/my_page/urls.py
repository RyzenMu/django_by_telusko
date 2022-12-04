from django.urls import path 
from . import views

urlpatterns= [ 
    path('', views.home, name='home'),
    path('my_page_1', views.my_page_1, name='home')
]