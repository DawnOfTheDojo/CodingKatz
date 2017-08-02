from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^profile', views.profile, name="profile"),
    url(r'^edit', views.edit, name="edit"),
    url(r'^delete', views.delete, name="delete"),
]
