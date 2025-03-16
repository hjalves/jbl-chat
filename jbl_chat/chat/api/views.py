from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from chat.api.serializers import MessageSerializer, ProfileSerializer
from chat.models import Message, Profile


class ChatMessagesAPIView(ListCreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        nickname = self.kwargs.get("nickname")
        current_profile = self.request.user.profile
        other_profile = get_object_or_404(Profile, nickname=nickname)
        return Message.objects.conversation_between(current_profile, other_profile)

    def perform_create(self, serializer):
        receiver = get_object_or_404(Profile, nickname=self.kwargs.get("nickname"))
        serializer.save(sender=self.request.user.profile, receiver=receiver)


class UserListApiView(ListAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [IsAuthenticated]
