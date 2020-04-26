from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^signUp$', views.signUp),
    url(r'^signIn$', views.signIn),
    url(r'^showEvents$', views.showEvents),
    url(r'^showEventUser$', views.showEventUser),
    url(r'^addEvent$', views.addEvent),
    url(r'^addEventUser$', views.addEventUser),
    url(r'^removeEventUser$', views.removeEventUser),
]