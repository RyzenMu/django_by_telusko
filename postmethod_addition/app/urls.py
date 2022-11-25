from django.urls import path 
from . import views

urlpatterns = [ 
    path('', views.first_page, name='page1'),
    path('addition', views.addition_page, name='page2')
]