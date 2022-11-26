from django.urls import path 
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [ 
    path('', views.home_page, name='page0'),
    path('makemytrip', views.makemytrip, name='page1'),
    path('kaveri', views.kaveri, name='kaveri')
]

urlpatterns += staticfiles_urlpatterns()

