from django.db import models
from email.policy import default
from django.db import models
from users.models import User

class Constants:
    connections_choices = [
        ("a", 'accepted'),
        ('r', 'requested'),
        ('d', 'declined'),
        ('b', "blocked")
    ]
    messages_choices = [
        ('pdf', 'pdf'),
        ('photo', 'photo'),
        ('message', 'message'),
        ('map', 'map'),
        ('contact', 'contact'),
        ('file', 'file')
    ]
    chat_type = [
        ('group', 'group'),
        ('chat', 'chat'),

    ]

class Friends(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(User, related_name='sender_friends', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='receiver_friends', on_delete=models.CASCADE)
    status = models.CharField(max_length=255, choices=Constants.connections_choices)


class Group(models.Model):
    group_icon = models.TextField()
    created_by = models.ForeignKey(User, related_name='group_created_by', on_delete=models.CASCADE)
    last_modified_by = models.ForeignKey(User, related_name='group_modified_by', on_delete=models.CASCADE)
    group_name = models.CharField(max_length=255)


class GroupMembers(models.Model):
    group_id = models.ForeignKey(Group, related_name='group_member', on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, related_name='group_user', on_delete=models.CASCADE)


class Messages(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(User, related_name='sender_messages', on_delete=models.CASCADE)
    chat_receiver = models.ForeignKey(User, related_name='receiver_messages', null=True, on_delete=models.CASCADE)
    group_receiver = models.ForeignKey(Group, related_name='group_messages', null=True, on_delete=models.CASCADE)
    message = models.TextField()
    message_type = models.CharField(max_length=255, choices=Constants.messages_choices)
    seen = models.JSONField()
    chat_type = models.CharField(max_length=255, choices=Constants.chat_type)
