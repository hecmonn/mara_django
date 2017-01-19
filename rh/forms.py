from django import forms
from django.db import models
from .models import Empleados,Sucursales

class EmpleadosForm(forms.ModelForm):
    class Meta:
        model=Empleados
        exclude=[]
        labels={
            'bod':'Fecha de nacimiento',
            'rfc':'RFC'
        }
        widgets={
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'estado':forms.Select(attrs={'class':'form-control'}),
            'sexo':forms.RadioSelect(attrs={'class':'form-control'}),
            'telefono':forms.TextInput(attrs={'class':'form-control'}),
            'curp':forms.TextInput(attrs={'class':'form-control'}),
            'no_imss':forms.TextInput(attrs={'class':'form-control'}),
            'bod':forms.SelectDateWidget(attrs={'class':'form-control'}),
            'imss':forms.TextInput(attrs={'class':'form-control'}),
            'puesto':forms.Select(attrs={'class':'form-control'}),
            'sueldo':forms.NumberInput(attrs={'class':'form-control'}),
            'direccion':forms.TextInput(attrs={'class':'form-control'}),
            'rfc':forms.TextInput(attrs={'class':'form-control'}),
            'sucursal':forms.Select(attrs={'class':'form-control'}),
            'infonavit':forms.TextInput(attrs={'class':'form-control'})
        }

class SucursalesForm(forms.ModelForm):
    class Meta:
        model=Sucursales
        exclude=[]
