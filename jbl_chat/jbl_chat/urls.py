"""
jbl_chat URL Configuration
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from chat import views as chat_views

urlpatterns = [
    path("", include("chat.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("mock-page/", chat_views.mock_page, name="mock-page"),
    path("mock-messages/", chat_views.mock_messages, name="mock-messages"),
    path("admin/", admin.site.urls),
]
