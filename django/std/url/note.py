from django.conf.urls import patterns, url
from notes import views

urlpatterns = patterns('notes.note.views',url(r'^add$', views.NoteCreate.as_view(), name='note-create'),
                       url(r'^mail$', views.CreateNoteByMail.as_view(), name='note-create-by-mail'),
                       url(r'^get$', views.MyNoteList.as_view(), name='note-list'),
                       url(r'^decrypt/(?P<pk>\d+)$', views.NoteDecrypt.as_view(), name='note-decrypt'),
                       url(r'^get/archived$', views.MyArchivedNoteList.as_view(), name='archived-note-list'),
                       url(r'^del/(?P<pk>\d+)$', views.NoteDel.as_view(), name='note-del'),
                       url(r'^patch/(?P<pk>\d+)$', views.NotePatch.as_view(), name='note-patch'),
                       url(r'^versions/(?P<pk>\d+)$', views.NoteVersion.as_view(), name='note-versions'),
                       url(r'^revert$', views.NoteRevert.as_view(), name='note-revert'),
                       url(r'^search/(?P<search>[A-Za-z0-9\.\s\-_]+)$', views.NoteListSearch.as_view(), name='notes-list-search'),
                       url(r'^comments/add$', views.AddComment.as_view(), name='comment-create'),
                       url(r'^comments/del/(?P<pk>\d+)$', views.DelComment.as_view(), name='comment-delete'),
                       url(r'^comments/get/(?P<note>\d+)$', views.GetComment.as_view(), name='comment-get-by-note'),
                       )