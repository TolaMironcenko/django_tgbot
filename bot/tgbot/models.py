from django.db import models


class UserInfo(models.Model):
    # Name = models.CharField(max_length=25)
    userName = models.CharField(max_length=25)
    userId = models.BigIntegerField()


class Message(models.Model):
    Message_text = models.TextField()
    # who_message_ids = ?
    when_message = models.DateTimeField()
