"""
jbl_chat URL Configuration
"""

from django.contrib import admin
from django.urls import path

from chat import views as chat_views

urlpatterns = [
    path("", chat_views.hello_world, name="hello-world"),
    path("mock-page/", chat_views.mock_page, name="mock-page"),
    path("mock-messages/", chat_views.mock_messages, name="mock-messages"),
    path("admin/", admin.site.urls),
]
