from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from django.db.models import Q
from django.utils.formats import localize


class Profile(models.Model):
    """
    A member profile for a user of the chat application.
    """

    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    # The nickname is used to uniquely identify a member in the chat application.
    nickname = models.SlugField(max_length=30, unique=True)
    # The last time the user was seen online.
    last_seen = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "profile"
        verbose_name_plural = "profiles"
        ordering = ["nickname"]

    def __str__(self):
        return self.nickname

    def full_name(self):
        return self.user.get_full_name()


class MessageManager(models.Manager):
    def conversation_between(self, profile1, profile2):
        """
        Return a queryset of messages exchanged between two profiles.
        """
        return self.filter(
            Q(sender=profile1, receiver=profile2) | Q(sender=profile2, receiver=profile1)
        )


class Message(models.Model):
    """
    A message sent from one member to another.
    """

    objects = MessageManager()

    sender = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="sent_messages"
    )
    receiver = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="received_messages"
    )
    content = models.TextField(max_length=settings.MAX_MESSAGE_LENGTH)
    timestamp = models.DateTimeField(auto_now_add=True)
    read_at = models.DateTimeField(
        null=True,
        blank=True,
        help_text="The time the message was marked as read, by the receiver.",
    )

    class Meta:
        verbose_name = "message"
        verbose_name_plural = "messages"
        ordering = ["timestamp"]

    def __str__(self):
        return (
            f"Message from {self.sender} to {self.receiver} at "
            f"{localize(self.timestamp)}: {self.content_preview()}"
        )

    def content_preview(self, length=50):
        return (
            self.content[:length] + "..." if len(self.content) > length else self.content
        )
