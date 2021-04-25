from django.contrib.auth import get_user_model
from django.db import models

from chat_users.models import ChatUser

User = get_user_model()


class Contacts(models.Model):
    belongs_to = models.OneToOneField(ChatUser, related_name="contact_user", on_delete=models.CASCADE)
    friends_list = models.ManyToManyField(ChatUser, related_name="user_friends", blank=True)

    def __str__(self):
        friends = ""
        for friend in self.friends_list.all():
            friends+= str(friend) + ", "
            print(friend)
        return f"Belongs to : {self.belongs_to} -- Friends: {friends} "


class Messages(models.Model):
    author = models.ForeignKey(ChatUser, related_name= "message_belongs_to", on_delete=models.CASCADE)
    msg = models.TextField('message', max_length=256, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message id :{self.pk}"

class ChatHistory(models.Model):
    participants = models.ManyToManyField(ChatUser, related_name="history_participants",  blank=True)
    messages = models.ManyToManyField(Messages, related_name="messages", blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"participants : "
class LoggedInUser(models.Model):
    user = models.OneToOneField(ChatUser, related_name="logger_user", on_delete=models.CASCADE)
