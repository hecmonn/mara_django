from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index,name="index"),
    url(r'^captura$',views.captura,name="captura"),
    url(r'^create-articulo$',views.create_articulo),
    url(r'^articulos$',views.articulos,name='articulos')
]
