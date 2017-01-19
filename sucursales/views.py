from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from finanzas.models import Av
from .forms import *

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect('')
    return render(request,'sucursales/login.html')
def index(request):
    context={
        'active_suc':'active'
    }
    return render(request,'sucursales/index.html',context)

def av(request):
    context={
        'titulo':'Captura',
        'active_av':'active',
        'form':AvForm,
    }
    return render(request,'sucursales/av.html',context)

#forms
def av_create(request):
    pass
