from django import forms
from .models import (
    AuctionListing,
    Category,
    Bids,
    Comments,
)

def higher_bid(current_highest_bid, bid_from_user):
    return False



class AuctionCreationForm(forms.ModelForm):
    class Meta:
        model = AuctionListing
        #fields = '__all__'
        exclude = ('created_by','time_created','active',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ('listing','created_by',)


class BidForm(forms.ModelForm):
    offered_price = forms.IntegerField()
    class Meta:
        model = Bids
        fields = ('offered_price',) 

    