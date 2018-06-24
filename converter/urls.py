from django.conf.urls import url
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^link/new/$', views.link_new, name='link_new'),
    url(r'^submit/$', views.link_new, name='index')
]