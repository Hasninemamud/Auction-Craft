# Generated by Django 5.0.4 on 2024-04-28 09:41

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0018_alter_user_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='listing',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]