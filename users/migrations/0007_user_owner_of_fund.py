# Generated by Django 4.2.5 on 2023-09-30 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0002_initial'),
        ('users', '0006_user_is_fond_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='owner_of_fund',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organisations.fund'),
        ),
    ]