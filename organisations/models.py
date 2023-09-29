from django.db import models

from users.models import User


class Organisation(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=255)
    summary = models.PositiveIntegerField(default=0)
    OGRN = models.PositiveIntegerField(max_length=14)
    is_verified = models.BooleanField(default=False)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)

