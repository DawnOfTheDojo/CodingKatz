from django.conf.urls import url
from . import views

app_name="User"

urlpatterns = [
    url(r'^profile', views.profile, name="profile"),
    url(r'^edit', views.edit, name="edit"),
    url(r'^delete', views.delete, name="delete"),
]
