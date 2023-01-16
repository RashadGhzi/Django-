from django.shortcuts import render,redirect,HttpResponse
from .models import Authentication

# Create your views here.
def index(request):
    em = Authentication.objects.all()
    context = {
        'em':em
    }
    return render(request,'index.html', )

def auth(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.ge('lname')
        username = request.POST.get('username')
        password = request.POST.get('fname')
        retype_password = request.POST.get('retype_password')

        myuser = Authentication(
            first_name = fname,
            last_name = lname,
            username = username,
            password = password,
            retype_password = retype_password
        )
        myuser.save()
        return redirect('/')

    else:
        return HttpResponse('error')


