from django.conf.urls import patterns, url
from notes import views

urlpatterns = patterns('', url(r'^upload/file$', views.UploadFile.as_view(), name='upload-file'),
                       url(r'^upload/pic$', views.UploadPic.as_view(), name='upload-profile-pic'),
                       # url(r'^upload/pic/patch(?P<pk>)\d+$', views.UploadPic.as_view(), name='upload-profile-pic'),
                       # url(r'^upload/pic/del(?P<pk>)\d+$', views.UploadPic.as_view(), name='upload-profile-pic'),
                       url(r'^upload/boardpic(?P<boardid>\d+)$', views.UploadBoardPic.as_view(), name='upload-board-pic'),
                       url(r'^upload/boardcoverpic(?P<boardid>\d+)$', views.UploadBoardCoverPic.as_view(), name='upload-board-cover-pic'),
                       # url(r'^upload/boardpic/patch(?P<pk>)\d+$', views.UploadPic.as_view(), name='upload-profile-pic'),
                       # url(r'^upload/boardpic/del(?P<pk>)\d+$', views.UploadPic.as_view(), name='upload-profile-pic'),
                       )