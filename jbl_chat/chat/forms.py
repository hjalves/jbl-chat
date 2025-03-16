from django import forms
from django.forms import ModelForm

from chat.models import Message


class ChatForm(ModelForm):
    class Meta:
        model = Message
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(
                attrs={"placeholder": "Type a message...", "rows": 5}
            ),
        }
