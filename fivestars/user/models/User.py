# -*- coding: utf-8 -*-
import re

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.core import validators
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(UserManager):
    use_in_migrations = False
    def _create_user(self, phone_number, name, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = timezone.now()
        if not phone_number:
            raise ValueError('The given phone_number must be set')
        user = self.model(phone_number=phone_number, name=name,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, name, password, **extra_fields):
        return self._create_user(phone_number, name, password, True, True,
                                 **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username, password and email are required. Other fields are optional.
    """
    phone_number = models.CharField(_('phone_number'), max_length=15, unique=True)
    name = models.CharField(_('name'), max_length=254,
                            help_text=_('Required. 254 characters or fewer. Letters, numbers and '
                                        '@/./+/-/_ characters'),
                            validators=[
                                validators.RegexValidator(re.compile('^[\w.@+-]+$'), _('Enter a valid name.'),
                                                          'invalid')
                            ])
    email = models.EmailField(_('email address'), blank=True)
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin '
                                               'site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.'))

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['name',]

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.name)

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        return "A user called %s" % self.name

    def get_short_name(self):
        "Returns the short name for the user."
        return self.name

    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email])
