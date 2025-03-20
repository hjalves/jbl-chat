from django.contrib.auth.models import User
from rest_framework import serializers

from chat.models import Message, Profile


class ChatSerializer(serializers.ModelSerializer):
    total_messages = serializers.SerializerMethodField()
    last_contact = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ["username", "total_messages", "last_contact"]
        read_only_fields = ["username", "total_messages", "last_contact"]

    def get_total_messages(self, obj):
        request = self.context.get("request")
        current_profile = request.user.profile
        messages = Message.objects.conversation_between(current_profile, obj)
        return len(messages)

    def get_last_contact(self, obj):
        request = self.context.get("request")
        current_profile = request.user.profile
        messages = Message.objects.conversation_between(current_profile, obj)
        if messages.exists():
            return messages.latest("timestamp").timestamp
        return None


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["username", "full_name", "last_seen"]
        read_only_fields = ["username", "full_name", "last_seen"]


class CurrentUserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["username", "full_name", "email", "is_staff"]
        read_only_fields = ["username", "full_name", "email", "is_staff"]

    def get_full_name(self, obj):
        return obj.get_full_name()


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(
        source="sender.user", slug_field="username", read_only=True
    )
    receiver = serializers.SlugRelatedField(
        source="receiver.user", slug_field="username", read_only=True
    )

    class Meta:
        model = Message
        fields = "__all__"
        read_only_fields = ["sender", "receiver", "timestamp", "read_at"]
