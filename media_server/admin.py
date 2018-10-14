from django.contrib import admin
from django.conf import settings
from . import models

if settings.MEDIA_SERVER:
    
    @admin.register(models.Picture)
    class Picture(admin.ModelAdmin):
        list_display = ('title', 'upload_date')
