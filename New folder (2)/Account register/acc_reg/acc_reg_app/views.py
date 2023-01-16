from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from .models import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def handleRegister(request):
    if request.method == ["POST"]:
        name = request.POST.get['name']
        username = request.POST.get['username']
        email = request.POST.get['email']
        password = request.POST.get['password']
        repeat_password = request.POST.get['repeat_password']

        myuser = RegisterForm(
            name = name,
            username = username,
            email = email,
            password = password,
            repeat_password = repeat_password,
        )
        myuser.save()
        return redirect('home')
    return HttpResponse('404 - error')

        