from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from  django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.mail import send_mail

# Create your models here.
class MyUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user( email, password, **extra_fields)

    def create_superuser(self,  email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user( email, password, **extra_fields)

class ChatUser(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()
    first_name = models.CharField('first name', max_length=30, blank=True)
    last_name = models.CharField('last name', max_length=20, blank=True)
    email = models.EmailField('Email', unique=True)
    pic = models.ImageField('Profile Photo', upload_to='pic/%Y/%m/%d' , blank=False)
    phone_number = PhoneNumberField('Phone Number', unique=True)
    is_staff = models.BooleanField('staff status', default=False,
                                   help_text='Check whether user can access admin site')
    is_active = models.BooleanField('Active status', default=True,
                                    help_text='Check whether user in active or not')
    date_joined = models.DateTimeField('Joined date', default=timezone.now)

    objects = MyUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number', 'first_name']
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        swappable = 'AUTH_USER_MODEL'
    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return f"{self.get_full_name()}"