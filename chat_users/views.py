from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.views import View
from django.shortcuts import render, redirect
from chat_users.forms import SignUpForm, LoginForm
from chat_users.models import ChatUser
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

# Create your views here.
class SignUp(View):
    form_class = SignUpForm
    template_name = 'signup.html'
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        for element in form:
            print(element, element.id_for_label)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            # <process form cleaned data>
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            re_password = form.cleaned_data['re_password']
            phone_number = '+91' + str(form.cleaned_data['phone_number'])
            pic= form.cleaned_data['pic']

            if ChatUser.objects.filter(email=email).exists():
                messages.info(request, "Email already registered")
            elif ChatUser.objects.filter(phone_number=phone_number):
                messages.info(request, 'Mobile number already registered')
            else:
                if (password == re_password):

                    user = ChatUser.objects.create_user(first_name=first_name, last_name=last_name, email=email,
                                                         password=password, phone_number=phone_number, pic=pic)
                    user.save()
                    return HttpResponseRedirect('/users/login')
                else:
                    messages.info(request, "Password mismatching")

        return render(request, self.template_name, {'form': form})
class Login(View):
    template_name = 'login.html'
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        for element in form:
            print(element, element.id_for_label)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user:
                auth.login(request, user)
                return redirect('/chat')
            else:
                messages.info(request, "Wrong username or password")
        return render(request, self.template_name, {'form': form})


@login_required(login_url="/users/login")
def logout(request):
    auth.logout(request)
    return redirect('/')
