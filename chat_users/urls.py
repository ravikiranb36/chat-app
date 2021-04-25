from django.urls import path, include, re_path

from chat_app.views import IndexView
from chat_users.views import SignUp, Login, logout
from django.conf.urls.static import static
from chat_project.settings import MEDIA_ROOT, MEDIA_URL, STATIC_URL, STATIC_ROOT

urlpatterns = [
    path('signup', SignUp.as_view(), name = 'Sign up'),
    path('login', Login.as_view(), name = 'Login'),
    path('logout', logout, name = 'logout' ),
    # re_path(r"^.*", IndexView.as_view(), name='index'),
]
urlpatterns+= static(STATIC_ROOT, document_root = STATIC_ROOT)
urlpatterns+= static(MEDIA_URL, document_root = MEDIA_ROOT)