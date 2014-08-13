from django.conf.urls import patterns, url
from notes import views

urlpatterns = patterns('', url(r'^registerinvite/(?P<boardname>[A-Za-z0-9\.\s\-_]+)$', views.addShareToBoard.as_view(), name='add-share-to-board'),
                       url(r'^register$', views.UserCreate.as_view(), name='create-user'),
                       url(r'^verify$', views.verifyUser.as_view(), name='verify-user'),
                       url(r'^reverify$', views.reVerifyUser.as_view(), name='re-verify-user'),
                       url(r'^sendPasswordMail$', views.sendResetPassMail.as_view(), name='send-password-mail'),
                       url(r'^resetPassword$', views.resetUserPass.as_view(), name='reset-user-password'),
                       url(r'^unregister/(?P<pk>\d+)$', views.UserDel.as_view(), name='del-user'),
                       url(r'^log$', views.UserLog.as_view(), name='user-log'),
                       url(r'^before_register$', views.TempEmailCreate.as_view(), name='create-temp-user'),
                       url(r'^event/add$', views.registerToEvent.as_view(), name='register-to-event'),
                       url(r'^event/del/(?P<object_id>\d+)$', views.unRegisterFromEvent.as_view(), name='unregister-from-event'),
                       url(r'^notifications$', views.UserNotification.as_view(), name='get-notification'),
                       )