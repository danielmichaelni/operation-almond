from django.conf.urls import patterns, url
from foodmarket import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^browse/$', views.browse, name='browse'),
    url(r'^kitchen/$', views.kitchen, name='kitchen'),
    url(r'^kitchen/add/$', views.add_inventory, name='add_inventory'),
)