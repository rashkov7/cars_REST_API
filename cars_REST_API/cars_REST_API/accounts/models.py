from datetime import datetime, timedelta

import jwt
from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User, PermissionsMixin
from django.db import models

from django.utils import timezone

from cars_REST_API.accounts.managers import CustomManager


class CustomUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
        unique=True,
        error_messages={
            "unique": "A user with that username already exists."
        }
    )

    is_staff = models.BooleanField(
        "staff status",
        default=False,
        help_text="Designates whether the user can log into this admin site.",
    )
    is_active = models.BooleanField(
        "active",
        default=True,
        help_text=
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
    )
    date_joined = models.DateTimeField("date joined", default=timezone.now)

    objects = CustomManager()

    USERNAME_FIELD = "email"

    @property
    def token(self):
        token = jwt.encode({
            'email': self.email,
            "password": self.password,
            'exp': datetime.utcnow() + timedelta(hours=24)
        }, settings.SECRET_KEY, algorithm='HS256')
        return token


class ProfileModel(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.PositiveIntegerField()

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
