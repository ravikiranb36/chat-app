from django.contrib import admin

from chat_app.models import Contacts, Messages, ChatHistory

admin.site.register(Contacts)
admin.site.register(Messages)
admin.site.register(ChatHistory)
