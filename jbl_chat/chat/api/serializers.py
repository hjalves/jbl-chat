from rest_framework import serializers

from chat.models import Message, Profile


class ChatSerializer(serializers.ModelSerializer):
    total_messages = serializers.SerializerMethodField()
    last_contact = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ["nickname", "total_messages", "last_contact"]
        read_only_fields = ["nickname", "total_messages", "last_contact"]

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
        fields = ["nickname", "full_name", "last_seen"]
        read_only_fields = ["nickname", "full_name", "last_seen"]


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
