from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User, PermissionsMixin
from django.db import models

from django.utils import timezone

from cars_REST_API.accounts.managers import CustomManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)

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


class ProfileModel(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.PositiveIntegerField()

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
