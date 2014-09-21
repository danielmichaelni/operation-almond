from django.conf.urls import patterns, url
from foodmarket import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^browse/$', views.browse, name='browse'),
    url(r'^dish/(?P<dish_id>\d+)/$', views.dish_detail, name='dish_detail'),
    url(r'^dish/(?P<dish_id>\d+)/reviews/$', views.dish_reviews, name='dish_reviews'),
    url(r'^reviews/(?P<review_id>\d+)/$', views.review_detail, name='review_detail'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^kitchen/$', views.kitchen, name='kitchen'),
    url(r'^kitchen/add/$', views.add_inventory, name='add_inventory'),
    url(r'^venmo/$', views.venmo_authorization, name='venmo_authorization'),
)