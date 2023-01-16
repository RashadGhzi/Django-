from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('index',index, name='index'),
    path('datatable',datatable, name='datatable'),
    path('', log, name='log'),
    path('login', handleLogin, name='handleLogin'),
    path('logout',handleLogout, name='handleLogout'),
]