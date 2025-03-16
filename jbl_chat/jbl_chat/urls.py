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
    path("admin/", admin.site.urls),
]
