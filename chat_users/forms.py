from django import forms

def checksize(value):
    if len(value) < 6:
        raise forms.ValidationError("Password characters should be more than 6")

def phone_number_check(value) :
    if (len(str(value)) != 10) or (isinstance(value, int) == False):
        raise forms.ValidationError("Wrong phone number")

class SignUpForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    first_name = forms.CharField(label= 'First Name',
                                 widget=forms.TextInput(attrs={'placeholder':'First Name'}))
    last_name = forms.CharField(label= 'Last Name',
                                widget=forms.TextInput(attrs={'placeholder':'Last Name'}), required=False)
    email = forms.EmailField(label='Email',
                             widget=forms.TextInput(attrs={'placeholder':'Email Address'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
                               validators=[checksize,])
    re_password = forms.CharField(label='Re-password',
                               widget=forms.PasswordInput(attrs={'placeholder': 'Re-Password'}))
    phone_number = forms.IntegerField( widget=forms.TextInput(attrs={'placeholder':'Phone Number'}),
                                       validators=[phone_number_check, ], required=True)
    pic = forms.ImageField(label='Profile Photo', required=True)

class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    email = forms.EmailField(label='Email',
                             widget=forms.TextInput(attrs={'placeholder':'Email Address'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
                               validators=[checksize,])