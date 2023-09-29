# Generated by Django 4.2.5 on 2023-09-29 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_achievements_user_events_user_achievements'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(default='г. Москва, Ул. Ленина, д. 5, кв. 10', max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='post_index',
            field=models.PositiveIntegerField(default=101000),
        ),
        migrations.AddField(
            model_name='user',
            name='surname',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
