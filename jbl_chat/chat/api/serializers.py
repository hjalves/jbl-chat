from rest_framework import serializers

from chat.models import Message, Profile


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
