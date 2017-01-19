from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^av$',views.av,name='av'),
    url(r'^login$', views.login,name='login'),
    url(r'^av-create$',views.av_create,name="av_create")
]
