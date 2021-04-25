import json

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView

from chat_app.models import Contacts, Messages, ChatHistory, ChatUser

User = get_user_model()


@login_required(login_url="/users/login")
def chatroom(request):
    return render(request, "chatroom.html")


# Create your views here.
class ChatView(View):
    template_name = 'chat.html'

    def get(self, request, *args, **kwargs):
        history = ChatHistory.objects.filter(participants=request.user).order_by("-timestamp")
        context = {"historys": history}
        return render(request, self.template_name, context)


class IndexView(TemplateView):
    template_name = 'index.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class SaveMessage(View):
    def post(self, request, *args, **kwargs):
        sender = request.user
        historyId = request.POST["historyId"]
        message = request.POST["message"]
        print(historyId, message)
        msg = Messages(author=sender, msg=message)
        msg.save()
        history = get_object_or_404(ChatHistory, id=historyId)
        history.messages.add(msg)

        return HttpResponse("ok")


class GetChatHistory(View):
    def post(self, request, *args, **kwargs):
        historyId = request.POST["historyId"]
        history = get_object_or_404(ChatHistory, pk =historyId)
        messages = history.messages.all().order_by("timestamp")
        context = {"messages": messages, "history":history}
        return render(request, "chats.html", context)


class CheckContact(View):
    def post(self, request, *args, **kwargs):
        phone_number = "+91" + request.POST["phone_number"]
        user = get_object_or_404(ChatUser, phone_number=phone_number)
        result = "User is not registered to RVChat"

        if user:
            # print(request.user.contact_user.objects.all())
            if Contacts.objects.filter(belongs_to=request.user, friends_list=user).exists():
                result = "This phone number already in your contact"
                # return HttpResponse("This phone number already in your contact")
            else:
                contact, created = Contacts.objects.get_or_create(belongs_to=request.user)
                contact.friends_list.add(user)
                result = "This phone number added to your contacts"
                # return HttpResponse("This phone number added to your contacts")
        return  HttpResponse(json.dumps({"result" : result}))


class GetContacts(View):
    def post(self, request, *args, **kwargs):
        contact = get_object_or_404(Contacts, belongs_to=request.user)
        contacts = contact.friends_list.order_by("first_name").all()
        context = {"contacts": contacts}
        return render(request, "contacts.html", context)

class CreateHistory(View):
    def post(self, request, *args, **kwargs):
        phone_number = '+'+request.POST["phone_number"]
        print(phone_number)
        user = get_object_or_404(ChatUser, phone_number=phone_number)
        # history = ChatHistory.objects.filter( participants = Q(request.user) & Q(user))
        # if not history:
        history = ChatHistory()
        history.save()
        history.participants.add(request.user, user)
        partcipants = history.participants.all()
        return HttpResponse({"result":"history created successfully", "partcipants":partcipants})

