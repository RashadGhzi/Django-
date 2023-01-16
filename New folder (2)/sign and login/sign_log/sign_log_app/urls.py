from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('add/', add, name="add"),
    path('log/',log, name="log"),
    path('home/', home, name="home")
]