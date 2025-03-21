from django.contrib import admin

from chat.models import Profile, Message


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("username", "last_seen", "user")
    readonly_fields = ("last_seen", "username")
    raw_id_fields = ("user",)
    fields = (
        "user",
        "username",
        "last_seen",
    )


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("timestamp", "sender", "receiver", "content_preview")
    readonly_fields = ("timestamp",)
    search_fields = ("sender", "receiver", "content")
    ordering = ("-timestamp",)
    list_filter = ("timestamp", "sender", "receiver")
    fields = (
        "sender",
        "receiver",
        "content",
        "timestamp",
    )
