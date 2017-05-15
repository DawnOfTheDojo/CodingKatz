from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^user/', views.user),
    url(r'^edit', views.edit),
    url(r'^delete', views.delete),
]
