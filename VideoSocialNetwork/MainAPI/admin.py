from django.contrib import admin

from .models import *

class VSNUserAdmin(admin.ModelAdmin):
    list_display = ("user", "nickname",)

class VideoAdmin(admin.ModelAdmin):
    list_display = ("name", "channel", "preview")

class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "video", "text")

class ChannelAdmin(admin.ModelAdmin):
    list_display = ("name", "owner")

admin.site.register(VSNUser, VSNUserAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Channel, ChannelAdmin)
admin.site.register(Comment, CommentAdmin)
