from django.urls import path

from chat.views import index, ChatFormView, mock_page, mock_messages

app_name = "chat"
urlpatterns = [
    path("", index, name="index"),
    path("chats/<slug:nickname>/", ChatFormView.as_view(), name="chat"),
    path("mock-page/", mock_page, name="mock-page"),
    path("mock-messages/", mock_messages, name="mock-messages"),
]
