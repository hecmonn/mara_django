from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Empleados,Sucursales
from .forms import EmpleadosForm

def index(request):
    context={
        'active_rh':'active'
    }
    return render(request,'rh/index.html',context)

def empleados(request):
    empleados=Empleados.objects.all()
    titulo='Empleados'
    context={
        'empleados':empleados,
        'titulo':'Empleados',
        'active_em':'active'
    }
    return render(request,'rh/empleados.html',context)

def empleados_captura(request):
    titulo='Captura de empleado'
    return render(request,'rh/empleados_captura.html',{'form':EmpleadosForm,'titulo':titulo})

def sucursales(request):
    s=Sucursales.objects.all()
    context={
        'sucursales':s,
        'titulo':'Sucursales',
        'active_suc':'active'
    }
    return render(request,'rh/sucursales.html',context)
#forms submit
def empleado_create(request):
    if request.method=='POST':
        form=EmpleadosForm(request.POST)
        if form.is_valid():
            ne=form.save()
            return HttpResponseRedirect('empleados')
        else:
            empleados_captura()
