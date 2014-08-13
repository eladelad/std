from django.contrib import admin
from notes.models import *

admin.site.register(Note)
admin.site.register(Board)
admin.site.register(UserSettings)
admin.site.register(UserProfile)
admin.site.register(TempEmails)
admin.site.register(sendEmails)
admin.site.register(UploadedFile)
admin.site.register(UploadedImage)
admin.site.register(UploadedImageBoard)
admin.site.register(Comment)
admin.site.register(historyLog)
admin.site.register(eventRegister)
admin.site.register(notification)
# Register your models here.