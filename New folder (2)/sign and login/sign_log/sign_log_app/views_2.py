from django.shortcuts import render,HttpResponse,redirect
from .models import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate,login

# Create your views here.
def index(request):
    return render(request, 'index.html')

def home(request):
    if request.method == "POST":
        loginusername = request.POST.get("loginusername")
        loginpassword = request.POST.get("loginpassword")
        user = authenticate(request, username='loginusername', password='loginpassword')
        if user is not None:
            login(request, user)
            return HttpResponse('done')
    # A backend authenticated the credentials
        else:
            return HttpResponse('not done')
    return HttpResponse('Post is not working.')

def add(request):
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        username = request.POST.get("username")
        password = request.POST.get("password")
        repassword = request.POST.get("repassword")

        if password != repassword:
            messages.error(request,'password do not matched')
            return redirect('index')
        
        data_save = RegisterForm(
            first_name = fname,
            last_name = lname,
            username = username,
            password = password,
            retype_password = repassword
        )
        data_save.save()
        messages.success(request, 'You have done')
        return redirect('log')

    return HttpResponse('error')


def log(request):
    return render(request,'log.html')
