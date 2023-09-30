from django.db import models
from django.urls import reverse


class Organisation(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=255)
    summary = models.PositiveIntegerField(default=0)
    OGRN = models.PositiveIntegerField()
    is_verified = models.BooleanField(default=False)
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Department(models.Model):
    title = models.CharField(max_length=255)
    organisation = models.ForeignKey(Organisation,
                                     on_delete=models.CASCADE,
                                     related_name="departments")

    def __str__(self):
        return self.title


class Fund(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    donated = models.PositiveIntegerField(default=0)
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE)
    logo = models.ImageField(upload_to="fund-logos/%Y/%m/%d/")

    # def get_absolute_url(self):
    #     return reverse("organ")

    def __str__(self):
        return self.title
