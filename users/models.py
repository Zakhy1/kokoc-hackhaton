from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_boss = models.BooleanField(default=False)
    profile_image = models.ImageField(upload_to="profiles/%Y/%m/%d/")
    # events = models.ManyToManyField
