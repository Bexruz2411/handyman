from django.urls import path
from .views import *

urlpatterns =[
    path('', main, name='main'),
    path('about', about, name='about'),
    path('blog', blog, name='blog'),
    path('cars', cars, name='cars'),
    path('services', services, name='services'),
    path('single', single, name='single'),
]