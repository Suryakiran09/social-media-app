from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from inst_profile.models import Profile

class Message(models.Model):
    sender = models.ForeignKey(Profile, related_name='sent_messages', on_delete=models.CASCADE)
    recipients = models.ManyToManyField(Profile, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.sender.username} to {', '.join([recipient.username for recipient in self.recipients.all()])}"

class Group(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(Profile, related_name='groups')
    created_by = models.ForeignKey(Profile, related_name='created_groups', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name