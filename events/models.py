from django.db import models


class Activity(models.Model):
    title = models.CharField(max_length=128)


class Period(models.Model):
    start = models.DateField()
    end = models.DateField()


class Event(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=255)
    price = models.PositiveIntegerField(default=990)
    activity = models.ForeignKey(Activity,
                                 on_delete=models.CASCADE,
                                 related_name="activity")
    period = models.ForeignKey(Period,
                               on_delete=models.CASCADE,
                               related_name="period")


class ActivityProof(models.Model):
    user = models.ForeignKey("users.User",
                             on_delete=models.CASCADE,
                             related_name="users")
    activity = models.ForeignKey("Activity",
                                 on_delete=models.CASCADE,
                                 related_name="activities")
    screenshot = models.ImageField(upload_to="proofs/%Y/%m/%d/")
