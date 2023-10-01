from datetime import date

from django.db import models
from django.contrib.auth.models import AbstractUser

from events.models import Event
from organisations.models import Organisation, Department, Fund
from django.utils.translation import gettext_lazy as _

from users.manager import CustomUserManager


class Achievements(models.Model):
    title = models.CharField(max_length=255)
    icon = models.ImageField(upload_to="achievements/%Y/%m/%d/")
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title


class User(AbstractUser):
    username = None
    surname = models.CharField(max_length=255, blank=True, null=True)
    is_boss = models.BooleanField(default=False)
    is_fond_owner = models.BooleanField(default=False)
    profile_image = models.ImageField(upload_to="profiles/%Y/%m/%d/", blank=True, null=True)
    department = models.ForeignKey(Department,
                                   on_delete=models.CASCADE,
                                   related_name="departments",
                                   null=True, blank=True)
    owner_of_fund = models.ForeignKey(Fund, on_delete=models.CASCADE,
                                      null=True, blank=True)
    achievements = models.ManyToManyField(Achievements, blank=True)
    events = models.ManyToManyField(Event, blank=True)
    events_done = models.ManyToManyField(Event, blank=True, related_name="done")
    post_index = models.PositiveIntegerField(default=101000)
    address = models.CharField(max_length=255, default="г. Москва, Ул. Ленина, д. 5, кв. 10")

    email = models.EmailField(_("email address"), unique=True)
    date_of_birth = models.DateField(default=date.today)
    coins = models.PositiveIntegerField(default=0)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.surname}"
