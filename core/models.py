import secrets

from django.db import models

from django.db import models

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager, PermissionsMixin
from django.db import models


class UserMG(UserManager):
    def create_user(self, email=None, username=None, password=None, is_staff=False, is_superuser=False, **extra_fields):
        user = self.model(
            email=email,
            username=username,
            password=password,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(str(password))
        user.save()
        return user

    def create_superuser(self, email=None, username=None, password=None, **extra_fields):
        return self.create_user(
            username=username,
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True,
            **extra_fields
        )


class CustomUser(AbstractBaseUser, PermissionsMixin):
    # admin
    username = models.CharField(max_length=512, unique=True)
    email = models.EmailField(max_length=512, unique=True)

    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    user_type = models.SmallIntegerField(choices=[
        (1, "Admin"),
        (2, "User"),
    ], default=2)

    objects = UserMG()

    REQUIRED_FIELDS = ['email',]
    USERNAME_FIELD = 'username'


class OtpToken(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='otps')
    otp_code = models.CharField(max_length=6, default=secrets.token_hex(3))
    tp_created_at = models.DateTimeField(auto_now_add=True)
    otp_expires_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.user.username




























































































































