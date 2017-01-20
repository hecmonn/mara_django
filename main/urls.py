from django.conf.urls import url
from . import views
from django.conf.urls import include

urlpatterns=[
    url(r'^$',views.index,name='home'),
    url(r'^usuario-nuevo$',views.usuario_nuevo,name='usuario-nuevo'),

    #conditional login
    url(r'^login_resolver$',views.login_resolver, name='login_resolver')
]
