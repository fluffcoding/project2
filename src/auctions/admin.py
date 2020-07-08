from django.contrib import admin

from .models import (
    AuctionListing,
    Category,
    Bids,
    Comments,
    User,
)

admin.site.register(User)
admin.site.register(AuctionListing)
admin.site.register(Category)
admin.site.register(Bids)
admin.site.register(Comments)