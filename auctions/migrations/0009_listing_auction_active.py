# Generated by Django 4.1 on 2022-09-07 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_rename_price_bid_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='auction_active',
            field=models.BooleanField(default=False),
        ),
    ]