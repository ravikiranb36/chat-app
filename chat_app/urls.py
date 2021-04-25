from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.urls import path, re_path

from chat_app.views import ChatView, IndexView, AboutView, SaveMessage, GetChatHistory, CheckContact, GetContacts, \
    chatroom, CreateHistory
from chat_project.settings import STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT, LOGIN_URL

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('chat/', login_required(ChatView.as_view(), login_url=LOGIN_URL)),
    path('about', AboutView.as_view(), name='About'),
    path('save-message', SaveMessage.as_view(), name='save-message'),
    re_path("get-chat-history/", GetChatHistory.as_view(), name="Getting Chat History"),
    path("checkContact", CheckContact.as_view(), name="Check contact number"),
    path("getContacts", GetContacts.as_view(), name="Get contacts"),
    path("chatting", chatroom, name="chat room"),
    path("createHistory", CreateHistory.as_view(), name="create history"),

]
urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
