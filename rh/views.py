from django.shortcuts import render
from django.http import HttpResponse
from .models import Empleados
from .forms import EmpleadosForm

def index(request):
    return render(request,'rh/index.html')

def empleados(request):
    empleados=Empleados.objects.all()
    return render(request,'rh/empleados.html',{'empleados':empleados})

def empleados_captura(request):
    return render(request,'rh/empleados_captura.html',{'form':EmpleadosForm})
