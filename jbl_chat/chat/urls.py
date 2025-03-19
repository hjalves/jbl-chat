from django.urls import path, include
from django.views.generic import RedirectView

from chat.api.urls import api_urlpatterns
from chat.views import about, ChatFormView, mock_login

app_name = "chat"


urlpatterns = [
    path("", RedirectView.as_view(pattern_name="chat:about"), name="index"),
    path("about/", about, name="about"),
    path("mock/login/", mock_login, name="mock_login"),
    path("api/", include(api_urlpatterns)),
    path("chats/<slug:nickname>/", ChatFormView.as_view(), name="chat"),
]
