from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^wall', views.wall),
    url(r'^message', views.message),
    url(r'^comment', views.comment),
    url(r'^deleteMessage', views.deleteMessage),
    url(r'^deleteComment', views.deleteComment),
]
