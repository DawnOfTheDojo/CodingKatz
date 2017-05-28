from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^wall', views.wall, name="wall"),
    url(r'^message', views.message, name="message"),
    url(r'^comment', views.comment, name="comment"),
    url(r'^deleteMessage', views.deleteMessage, name="deleteMessage"),
    url(r'^deleteComment', views.deleteComment, name="deleteComment"),
]
