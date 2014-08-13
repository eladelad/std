from django.conf.urls import patterns, url
from notes import views

urlpatterns = patterns('',url(r'^files$', views.MyFileList.as_view(), name='my-file-list'),
                       url(r'^boards$', views.MyBoardList.as_view(), name='my-board-list'),
                       url(r'^boards/archived(?P<archived>)$', views.MyBoardList.as_view(), name='my-board-list'),
                       url(r'^boards/fav$', views.MyFavBoard.as_view(), name='my-fav-board-list'),
                       url(r'^boards/history$', views.MyHistoryBoard.as_view(), name='my-history-board-list'),
                       url(r'^notes$', views.MyNoteList.as_view(), name='my-note-list'),
                       url(r'^notes/recent$', views.MyRecentNotes.as_view(), name='my-recent-note-list'),
                       url(r'^settings$', views.MySettings.as_view(), name='my-settings'),
                       url(r'^settings/(?P<pk>\d+)$', views.MySettings.as_view(), name='patch-my-settings'),
                       url(r'^profile$', views.GetCurrentUser.as_view(), name='my-profile'),
                       url(r'^profile/patch/(?P<pk>\d+)$', views.GetCurrentUser.as_view(), name='patch-my-profile'),
                       )