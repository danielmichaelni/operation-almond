from django.conf.urls import patterns, url
from foodmarket import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)