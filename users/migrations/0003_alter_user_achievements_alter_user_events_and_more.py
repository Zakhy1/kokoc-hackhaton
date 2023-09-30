# Generated by Django 4.2.5 on 2023-09-30 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_initial'),
        ('users', '0002_alter_user_managers_remove_user_username_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='achievements',
            field=models.ManyToManyField(blank=True, null=True, to='users.achievements'),
        ),
        migrations.AlterField(
            model_name='user',
            name='events',
            field=models.ManyToManyField(blank=True, null=True, to='events.event'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='profiles/%Y/%m/%d/'),
        ),
    ]
