from django.shortcuts import render,HttpResponse,redirect
from .models import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate,login

# Create your views her
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
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        username = request.POST["username"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        if len(fname)<=5 or len(lname)<=5 or len(username)<=5:
            messages.error(request, "Your input should be greater then 5")
            return redirect('index')

        
        else:   
            data_save = RegisterForm(
                first_name = fname,
                last_name = lname,
                username = username,
                password = password,
                retype_password = repassword
            )
            data_save.save()
            return redirect('log')

    return HttpResponse('error')


def log(request):
    return render(request,'log.html')
