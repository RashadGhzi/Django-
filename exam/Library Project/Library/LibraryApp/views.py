from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from random import randint
from Library.settings import *
from django.contrib import messages
from .models import BooksAdd,BookLend
from datetime import datetime,timedelta
from .form import BooksAddForm
# Create your views here.

def sign(request):
    return render(request, 'auth/sign.html')

def log(request):
    return render(request, 'auth/log.html')

def book_shop(request):

    books = BooksAdd.objects.all()
    context = {
        'books':books,
    }
    return render(request, 'bookShop/bookShopHome.html',context)

verifyCode = {}
def sign_form(request):
    if request.method == 'POST':
        first_name = request.POST['firs_name'] 
        last_name = request.POST['last_name'] 
        username = request.POST['username'] 
        email = request.POST['email'] 
        password = request.POST['password'] 
        retype_password = request.POST['retype_password'] 
        verifyCode['email']=email
        
        if len(username)<4:
            messages.error(request,'Your username must be greater then 3 characters')
            return redirect('sign')
        elif password != retype_password:
            messages.error(request,'Your password is not matched')
            return redirect('sign')

        user = User.objects.create_user(username=username,email=email,password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        
        verifyCode['code'] = str(randint(5000,6000))
        subject = 'Authentication project'
        message = verifyCode['code']
        from_mail = EMAIL_HOST_USER
        to_mail = email
        send_mail(
        subject,
        message,
        from_mail,
        [to_mail],
        fail_silently=False,
        )
        return redirect('validationPg')

def validationPg(request):
    return render(request, 'auth/validationPg.html', verifyCode)

def verifyCodeForm(request):
    if request.method == 'POST':
        verifycd = request.POST['verifycd']
        if verifycd == verifyCode['code']:
            return redirect('log')
        messages.error(request, 'Invalid verification code') 
        return redirect('validationPg')

def logForm(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('book_shop')
        messages.error(request, 'Enter an valid username and password')
        return redirect('log')

def LogOut(request):
    logout(request)
    messages.success(request, "You have successfully logout.")
    return redirect("book_shop")

def about(request):
    return render(request, 'bookShop/about.html')

def contactUs(request):
    return render(request, 'bookShop/contact.html')

def bookLend(request):
    return render(request, 'auth/bookLendForm.html')

def bookLendForm(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        lend_date = datetime.now()
        dt = lend_date + timedelta(days=7)

        book_lend = BookLend(
            full_name = full_name,
            email = email,
            phone_number = phone_number,
            address = address,
            to_date = dt
        )
        book_lend.save()
        user_data = BookLend.objects.filter(full_name=full_name)
        print(user_data)
        subject = 'Our Library website'
        message = f"Hello {full_name}, Thank you for choosing our library managment website.We will happy be to see you again. Your book request date is {lend_date} and return date is {dt}. If you didn't return this book at this time we will add fine in your account."
        from_mail = EMAIL_HOST_USER
        to_mail = email
        send_mail(
        subject,
        message,
        from_mail,
        [to_mail],
        fail_silently=False,
        )
        messages.success(request, 'You have 7 days to return this book. We have sent you a mail.')
        return redirect('/')
    return redirect('bookLendForm')

def addBook(request):
    form = BooksAddForm(label_suffix=' ')
    return render(request,'auth/addBook.html',{'form':form})

def addBookForm(request):
    if request.method == 'POST':
        form = BooksAddForm(request.POST, request.FILES,)
        if form.is_valid():
            form.save()
            messages.success(request,'Your book added successfully on our site.')
            return redirect('/')
        
    messages.error(request,'Enter valid book info.')
    return redirect('addBook')
