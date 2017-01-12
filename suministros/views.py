from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import ArticuloForm

def index(request):
    return render(request,'suministros/index.html')

def captura(request):
    return render(request,'suministros/captura.html',{'form':ArticuloForm})

#forms
def create_articulo(request):
    if request.method=='POST':
        form=ArticuloForm(request.POST)
        if form.is_valid():
            nf=form.save(commit=False)
            nf.sucursal_id=1
            nf.save()
            return HttpResponseRedirect('/suministros')
    else:
        form=ArticuloForm()
    return render(request,'suministros/captura.html',{'form':form})
