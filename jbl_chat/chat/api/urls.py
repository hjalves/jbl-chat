from django.urls import path

from chat.api.views import (
    ChatMessagesAPIView,
    UserListApiView,
    UserDetailApiView,
    CurrentUserApiView,
    ChatListApiView,
    ChatDetailApiView,
)
from chat.views import api_index

api_urlpatterns = [
    path("chats/", ChatListApiView.as_view()),
    path("chats/<slug:username>/", ChatDetailApiView.as_view()),
    path("chats/<slug:username>/messages/", ChatMessagesAPIView.as_view()),
    path("users/", UserListApiView.as_view()),
    path("users/me/", CurrentUserApiView.as_view()),
    path("users/<slug:username>/", UserDetailApiView.as_view()),
]
