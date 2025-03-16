from django.urls import path, include

from chat.api.urls import api_urlpatterns
from chat.views import index, ChatFormView

app_name = "chat"


urlpatterns = [
    path("", index, name="index"),
    path("api/", include(api_urlpatterns)),
    path("chats/<slug:nickname>/", ChatFormView.as_view(), name="chat"),
]
