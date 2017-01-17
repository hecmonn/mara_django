from django.forms import ModelForm
from django.db import models
from .models import Empleados

class EmpleadosForm(ModelForm):
    class Meta:
        model=Empleados
        exclude=[]
