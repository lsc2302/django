from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^signUp$', views.sign_up),
    url(r'^signIn$', views.sign_in),
    url(r'^checkUserOnline$', views.check_user_online),
    url(r'^showEvents$', views.show_events),
    url(r'^showEventUser$', views.show_event_user),
    url(r'^addEvent$', views.add_event),
    url(r'^addEventUser$', views.add_event_user),
    url(r'^removeEventUser$', views.remove_event_user),
]