from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from chat.api.serializers import MessageSerializer, ProfileSerializer, ChatSerializer
from chat.models import Message, Profile


class UserListApiView(ListAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [IsAuthenticated]


class UserDetailApiView(RetrieveAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = "user__username"
    lookup_url_kwarg = "username"


class ChatListApiView(ListAPIView):
    serializer_class = ChatSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Profile.objects.exclude(user=self.request.user)


class ChatDetailApiView(RetrieveAPIView):
    serializer_class = ChatSerializer
    queryset = Profile.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = "user__username"
    lookup_url_kwarg = "nickname"


class ChatMessagesAPIView(ListCreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        nickname = self.kwargs.get("nickname")
        current_profile = self.request.user.profile
        other_profile = get_object_or_404(Profile, user__username=nickname)
        return Message.objects.conversation_between(current_profile, other_profile)

    def perform_create(self, serializer):
        receiver = get_object_or_404(Profile, user__username=self.kwargs.get("nickname"))
        serializer.save(sender=self.request.user.profile, receiver=receiver)
