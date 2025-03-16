from django.urls import path

from chat.api.views import ChatMessagesAPIView, UserListApiView

api_urlpatterns = [
    path("chats/", ChatMessagesAPIView.as_view()),
    path("chats/<slug:nickname>/messages/", ChatMessagesAPIView.as_view()),
    path("users/", UserListApiView.as_view()),
]
