# Generated by Django 4.2.5 on 2023-10-01 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0003_alter_fund_owner_alter_organisation_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fund',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='description',
            field=models.TextField(),
        ),
    ]
