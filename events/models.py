from django.db import models


class Activity(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Period(models.Model):
    start = models.DateField()
    end = models.DateField()

    def __str__(self):
        return f"{self.start} -> {self.end}"


class Event(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    price = models.PositiveIntegerField(default=990)
    activity = models.ForeignKey(Activity,
                                 on_delete=models.CASCADE,
                                 related_name="activity")
    period = models.ForeignKey(Period,
                               on_delete=models.CASCADE,
                               related_name="period")
    fund = models.ForeignKey("organisations.Fund",
                             on_delete=models.CASCADE,
                             related_name="funds")
    proof_needs = models.SmallIntegerField(default=0)
    coins = models.PositiveIntegerField(default=5)

    def __str__(self):
        return self.title


class EventProof(models.Model):
    user = models.ForeignKey("users.User",
                             on_delete=models.CASCADE,
                             related_name="users")
    event = models.ForeignKey("Event",
                              on_delete=models.CASCADE,
                              related_name="activities")
    screenshot = models.ImageField(upload_to="proofs/%Y/%m/%d/")
    сonfirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} - {self.event}"
