# Generated by Django 3.0.7 on 2020-07-05 07:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuctionListing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('starting_bid', models.FloatField()),
                ('image', models.ImageField(upload_to='auction_images')),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='category_images')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offered_price', models.FloatField()),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('auction_listing', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auctions.AuctionListing')),
                ('created_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='auctionlisting',
            name='category',
            field=models.ManyToManyField(to='auctions.Category'),
        ),
        migrations.AddField(
            model_name='auctionlisting',
            name='comments',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.Comments'),
        ),
        migrations.AddField(
            model_name='auctionlisting',
            name='created_by',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]