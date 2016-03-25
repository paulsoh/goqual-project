from django.contrib import admin

from video.models import Video


class VideoAdmin(admin.ModelAdmin):
    
    list_display = admin.ModelAdmin.list_display + (
       'title',
       'content',
       'url',
       'thumbnail',
       'source',
    )