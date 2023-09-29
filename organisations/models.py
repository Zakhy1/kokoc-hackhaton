from django.db import models


class Organisation(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=255)
    summary = models.PositiveIntegerField(default=0)
    OGRN = models.PositiveIntegerField()
    is_verified = models.BooleanField(default=False)
    owner = models.OneToOneField("users.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
