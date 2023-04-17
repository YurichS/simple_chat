from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.utils.timezone import now


# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(max_length=50, unique=True)
    objects = CustomUserManager

    def __str__(self):
        return self.email


class Thread(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    created = models.DateTimeField(default=now(), blank=True)
    updated = models.DateTimeField(default=now(), blank=True)

    def __str__(self):
        return str(self.id)


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    created = models.DateTimeField(default=now(), blank=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.text
