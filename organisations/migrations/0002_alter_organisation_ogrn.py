# Generated by Django 4.2.5 on 2023-09-29 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='OGRN',
            field=models.PositiveIntegerField(),
        ),
    ]