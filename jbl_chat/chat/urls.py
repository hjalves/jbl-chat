from django.urls import path, include

from chat.api.urls import api_urlpatterns
from chat.views import index, ChatFormView, mock_login

app_name = "chat"


urlpatterns = [
    path("", index, name="index"),
    path("mock/login/", mock_login, name="mock_login"),
    path("api/", include(api_urlpatterns)),
    path("chats/<slug:nickname>/", ChatFormView.as_view(), name="chat"),
]
