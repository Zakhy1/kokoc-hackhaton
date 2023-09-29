from django.db import models
from django.contrib.auth.models import AbstractUser

from organisations.models import Organisation


class User(AbstractUser):
    is_boss = models.BooleanField(default=False)
    profile_image = models.ImageField(upload_to="profiles/%Y/%m/%d/")
    company = models.ForeignKey(Organisation,
                                on_delete=models.CASCADE,
                                related_name="organisation",
                                null=True, blank=True)
    # events = models.ManyToManyField
