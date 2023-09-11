from django.contrib.auth.models import User
from django.db import models
from django.db.models import CheckConstraint, Q, F


class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=400)

    class Meta:
        constraints = [
            CheckConstraint(
                check=~Q(sender=F('recipient')),
                name='different_sender_recipient',
            ),
        ]
