from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,HttpRequest
from .forms import ArticuloForm
from .models import Articulos

def index(request):
    return render(request,'suministros/index.html')

def captura(request):
    return render(request,'suministros/captura.html',{'form':ArticuloForm})

def articulos(request):
    articles=Articulos.objects.all()
    return render(request,'suministros/articulos.html',{'articulos':articles})
#forms
def create_articulo(request):
    if request.method=='POST':
        form=ArticuloForm(request.POST)
        gastos=request.POST.get('cantidad[]')
        print gastos
        if form.is_valid():
            nf=form.save(commit=False)
            #nf.sucursal_id=1
            #nf.save(commit=False)
            return HttpResponseRedirect('/suministros')
    else:
        form=ArticuloForm()
    return render(request,'suministros/captura.html',{'form':form})
