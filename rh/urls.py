from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^empleados$',views.empleados,name='empleados'),
    url(r'^empleados_captura$',views.empleados_captura,name='em_cap'),
]
