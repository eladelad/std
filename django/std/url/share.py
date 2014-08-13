from django.conf.urls import patterns, url
from notes import views

urlpatterns = patterns('', url(r'^board/(?P<boardname>[A-Za-z0-9\.\s\-_]+)$', views.shareBoard.as_view(), name='share-board'),
                       url(r'^note$', views.SendNoteByMail.as_view(), name='share-note'),
                       )