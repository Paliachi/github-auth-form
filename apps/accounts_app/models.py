from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    past_address = models.CharField(max_length=255, null=True, blank=True)
    current_address = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.full_name
