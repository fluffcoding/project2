from django.contrib.auth.models import AbstractUser
from django.db import models

import datetime


class User(AbstractUser):
    watchlist = models.ManyToManyField('AuctionListing')


class AuctionListing(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()
    starting_bid = models.FloatField()
    image = models.URLField()
    category = models.ForeignKey('Category', on_delete=models.DO_NOTHING, null=True)
    time_created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)


    def __str__(self):
        return str(self.name) + str(self.created_by)


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    image = models.URLField()

    def __str__(self):
        return str(self.name)


class Bids(models.Model):
    auction_listing = models.ForeignKey(AuctionListing, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    offered_price = models.FloatField(null=False, blank=False)
    time_created = models.DateTimeField(auto_now_add=True)


class Comments(models.Model):
    listing = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()