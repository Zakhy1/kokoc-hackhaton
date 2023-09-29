from django.db import models
from django.contrib.auth.models import AbstractUser

from events.models import Event
from organisations.models import Organisation


class Achievements(models.Model):
    title = models.CharField(max_length=255)
    icon = models.ImageField(upload_to="achievements/%Y/%m/%d/")


class User(AbstractUser):
    is_boss = models.BooleanField(default=False)
    profile_image = models.ImageField(upload_to="profiles/%Y/%m/%d/")
    company = models.ForeignKey(Organisation,
                                on_delete=models.CASCADE,
                                related_name="organisation",
                                null=True, blank=True)
    achievements = models.ManyToManyField(Achievements)
    events = models.ManyToManyField(Event)
