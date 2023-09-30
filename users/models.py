from django.db import models
from django.contrib.auth.models import AbstractUser

from events.models import Event
from organisations.models import Organisation, Department


class Achievements(models.Model):
    title = models.CharField(max_length=255)
    icon = models.ImageField(upload_to="achievements/%Y/%m/%d/")
    description = models.CharField(max_length=255, blank=True, null=True)


class User(AbstractUser):
    surname = models.CharField(max_length=255, blank=True, null=True)
    is_boss = models.BooleanField(default=False)
    profile_image = models.ImageField(upload_to="profiles/%Y/%m/%d/")
    department = models.ForeignKey(Department,
                                   on_delete=models.CASCADE,
                                   related_name="departments",
                                   null=True, blank=True)
    achievements = models.ManyToManyField(Achievements)
    events = models.ManyToManyField(Event)
    post_index = models.PositiveIntegerField(default=101000)
    address = models.CharField(max_length=255, default="г. Москва, Ул. Ленина, д. 5, кв. 10")
