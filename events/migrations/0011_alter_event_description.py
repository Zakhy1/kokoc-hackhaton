# Generated by Django 4.2.5 on 2023-10-01 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_event_coins'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]