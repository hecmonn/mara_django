from django.shortcuts import render
from django.http import HttpRequest,HttpResponseRedirect
from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

def index(request):
    user=User.objects.all()
    h=User.objects.get(pk=1)
    print request.user
    context={
        'user':user,
    }
    return render(request,'main/index.html',context)

def usuario_nuevo(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')
        fn=request.POST.get('first_name')
        ln=request.POST.get('last_name')
        user=User.objects.create_user(username,email,password,last_name=ln,first_name=fn)
        return HttpResponseRedirect('/main')
    context={
        'titulo':'Nuevo usuario',
        'form':UserForm
    }
    return render(request,'main/user_create.html',context)

def login(request):
    context={}
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            context['session_message']="Welcome"
            return HttpResponseRedirect('/main')
        else:
            context['session_message']="Username/password incorrect"
    return render(request,'main/login.html',context)

#login resolver
def login_resolver(request):
    print request.user
    return HttpResponseRedirect('/main')
