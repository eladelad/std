from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from notes import views

urlpatterns = patterns('backend.views',
                       #url(r'^b/(?P<board>[A-Za-z0-9]+)/$', views.NoteListByBoard.as_view(), name='note-list-by-board'),
                       url(r'^note/', include('notes.url.note')),
                       url(r'^board/', include('notes.url.board')),
                       url(r'^user/', include('notes.url.user')),
                       url(r'^my/', include('notes.url.my')),
                       url(r'^share/', include('notes.url.share')),
                       url(r'^file/', include('notes.url.file')),
                       url(r'^general/', include('notes.url.general')),



)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += patterns('', url(r'^api-token-auth/', 'rest_framework.authtoken.views.obtain_auth_token'))
urlpatterns += patterns('',
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
)
urlpatterns = format_suffix_patterns(urlpatterns)
