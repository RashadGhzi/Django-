from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def datatable(request):
    return render(request,'datatable.html')

def log(request):
    return render(request,'log.html')

def handleLogin(request):
    return render('handleLogin')

def handleLogout(request):
    return render('handleLogout')