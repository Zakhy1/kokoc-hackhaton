# Generated by Django 4.2.5 on 2023-09-30 08:05

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0004_remove_activityproof_activity_activityproof_event'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ActivityProof',
            new_name='EventProof',
        ),
    ]
