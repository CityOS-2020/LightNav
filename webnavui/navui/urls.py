from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/navclick$', views.navclick, name='navclick'),
    url(r'^graph/lt$', views.usage_graph, name='usage_graph'),
]

