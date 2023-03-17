from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    def save(self, *args, **kwargs):
        super(Account, self).save(*args, **kwargs)
        if self.pk:
            Profile.objects.update_or_create(user_id=self.pk)
        return super(Account, self).save(*args, **kwargs)


class Profile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    past_address = models.CharField(max_length=255, null=True, blank=True)
    current_address = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=16, null=True, blank=True)

    def __str__(self):
        return self.user.username
