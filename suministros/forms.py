from django.forms import ModelForm,modelformset_factory
from django.db.models import CharField
from .models import Articulos

class ArticuloForm(ModelForm):
    articulo=CharField(
        max_length=50,
        help_text="Selecciona articulo"
    )
    class Meta:
        model=Articulos
        fields=['articulo','tipo']

class ArticuloFormset(ModelForm):
    pass
    #articulo=modelformset_factory(Articulos,exclude=())
