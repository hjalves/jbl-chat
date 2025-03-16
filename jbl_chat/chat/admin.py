from django.contrib import admin

from chat.models import Profile, Message


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("nickname", "last_seen", "user")
    search_fields = ("nickname",)
    readonly_fields = ("last_seen",)
    ordering = ("nickname",)
    raw_id_fields = ("user",)
    fields = (
        "user",
        "nickname",
        "last_seen",
    )


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("timestamp", "sender", "receiver", "content_preview")
    readonly_fields = ("timestamp", "read_at")
    search_fields = ("sender__nickname", "receiver__nickname", "content")
    ordering = ("-timestamp",)
    list_filter = ("timestamp",)
    fields = (
        "sender",
        "receiver",
        "content",
        "timestamp",
        "read_at",
    )
