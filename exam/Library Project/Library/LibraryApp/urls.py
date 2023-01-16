from django.contrib import admin
from django.urls import path
from .views import*
urlpatterns = [
    path('',book_shop, name='book_shop'),
    path('sign',sign, name='sign'),
    path('log', log, name='log'),
    path('signForm', sign_form, name='signForm'),
    path('validationPg', validationPg, name='validationPg'),
    path('verifyCodeForm', verifyCodeForm, name='verifyCodeForm'),
    path('logForm', logForm, name='logForm'),
    path('LogOut', LogOut, name='LogOut'),
    path('about/', about, name='about'),
    path('contactUs', contactUs, name='contactUs'),
    path('booklend/',bookLend, name='bookLend'),
    path('booklendform/', bookLendForm, name='bookLendForm'),
    path('addbook/', addBook, name='addBook'),
    path('addbookform/',addBookForm, name="addBookForm" )
]