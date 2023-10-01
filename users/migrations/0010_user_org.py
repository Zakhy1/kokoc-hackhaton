# Generated by Django 4.2.5 on 2023-10-01 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0003_alter_fund_owner_alter_organisation_owner'),
        ('users', '0009_user_coins'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='org',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='org', to='organisations.organisation'),
        ),
    ]
