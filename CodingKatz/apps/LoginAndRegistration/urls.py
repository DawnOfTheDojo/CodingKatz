from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^1$', views.index1),
    url(r'^2$', views.index2),
    url(r'^login', views.login),
    url(r'^first', views.first),
    url(r'^register', views.register),
]
