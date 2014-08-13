from django.conf.urls import patterns, url
from notes import views

urlpatterns = patterns('',url(r'^search/(?P<search>[A-Za-z0-9\.\s\-_]+)$', views.GeneralListSearch.as_view(), name='general-list-search'),
                       url(r'^tags', views.list_tags, name='list-tags'),
                       url(r'^counters', views.Counters.as_view(), name='counters'),
                       )