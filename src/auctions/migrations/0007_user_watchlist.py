# Generated by Django 3.0.7 on 2020-07-05 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_auto_20200705_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='watchlist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='auctions.AuctionListing'),
        ),
    ]