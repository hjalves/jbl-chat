from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from django.db.models import Q
from django.utils.formats import localize
from django.utils import timezone


class ProfileManager(models.Manager):
    def get_by_natural_key(self, nickname):
        return self.get(user__username=nickname)

    def online(self):
        """
        Return a queryset of profiles that have been seen online recently.
        """
        return self.filter(last_seen__gt=timezone.now() - settings.USER_LAST_SEEN_TIMEOUT)


class Profile(models.Model):
    """
    A member profile for a user of the chat application.
    """

    objects = ProfileManager()

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # The last time the user was seen online.
    last_seen = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "profile"
        verbose_name_plural = "profiles"
        ordering = ["user__username"]

    def __str__(self):
        return self.nickname()

    def natural_key(self):
        return (self.nickname(),)

    def nickname(self):
        return self.user.username

    nickname.short_description = "Nickname"
    nickname.admin_order_field = "user__username"

    def full_name(self):
        return self.user.get_full_name()


class MessageManager(models.Manager):
    def get_by_natural_key(self, sender_nickname, receiver_nickname, timestamp):
        sender = Profile.objects.get_by_natural_key(sender_nickname)
        receiver = Profile.objects.get_by_natural_key(receiver_nickname)
        return self.get(sender=sender, receiver=receiver, timestamp=timestamp)

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
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=settings.MAX_MESSAGE_LENGTH)

    class Meta:
        verbose_name = "message"
        verbose_name_plural = "messages"
        ordering = ["timestamp"]
        unique_together = ["sender", "receiver", "timestamp"]

    def natural_key(self):
        return (self.sender.nickname(), self.receiver.nickname(), self.timestamp)

    def __str__(self):
        return (
            f"Message from {self.sender} to {self.receiver} at "
            f"{localize(self.timestamp)}: {self.content_preview()}"
        )

    def content_preview(self, length=50):
        return (
            self.content[:length] + "..." if len(self.content) > length else self.content
        )
