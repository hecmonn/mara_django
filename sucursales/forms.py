from django import forms
from django.db import models
from finanzas.models import Av,Gastos

class AvForm(forms.ModelForm):
    class Meta:
        exclude=[]
        model=Av
        labels={
            'ticket1':'Ticket inicial',
            'ticket2':'Ticket Final',
            'bmx':'Banamex',
            'bbjio':'BanBajio',
            'amex':'American Express',
            'tot_tarjetas':'Total Tarjetas'
        }
        widgets={
            'ticket1':forms.NumberInput(attrs={'class':'form-control'}),
            'ticket2':forms.NumberInput(attrs={'class':'form-control'}),
            'bmx':forms.NumberInput(attrs={'class':'form-control'}),
            'bbjio':forms.NumberInput(attrs={'class':'form-control'}),
            'amex':forms.NumberInput(attrs={'class':'form-control'}),
            'santander':forms.NumberInput(attrs={'class':'form-control'}),
            'scotia_bank':forms.NumberInput(attrs={'class':'form-control'}),
            'money_card':forms.NumberInput(attrs={'class':'form-control'}),
            'univale':forms.NumberInput(attrs={'class':'form-control'}),
            'coppel':forms.NumberInput(attrs={'class':'form-control'}),
            'coupon_cloud':forms.NumberInput(attrs={'class':'form-control'}),
            'vales_caja':forms.NumberInput(attrs={'class':'form-control'}),
            'efectivo':forms.NumberInput(attrs={'class':'form-control'}),
            'dolares':forms.NumberInput(attrs={'class':'form-control'}),
            'tot_tarjetas':forms.NumberInput(attrs={'class':'form-control'}),
            'fondo':forms.NumberInput(attrs={'class':'form-control'}),
        }

    class GastosForm(forms.ModelForm):
        class Meta:
            model=Gastos
            exclude=[]
