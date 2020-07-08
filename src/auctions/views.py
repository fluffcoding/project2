from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required


from .models import User, AuctionListing, Comments, Category, Bids

from .forms import AuctionCreationForm, CommentForm, BidForm

@login_required
def index(request):
    auctions = AuctionListing.objects.filter(active=True)
    watchlist = request.user.watchlist.all()
    context = {
        'auctions': auctions,
        'watchlist': watchlist,
    }
    return render(request, "auctions/index.html", context)


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required
def auction_list_creation(request):
    form = AuctionCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            object = AuctionListing(**form.cleaned_data)
            object.created_by = request.user
            object.save()
            return redirect('/')
    context = {
        'form': form,
    }
    return render(request, 'auctions/create_auction.html', context)

@login_required

def single_auction_view(request, id):
    single_auction = get_object_or_404(AuctionListing, id=id)
    watchlist = request.user.watchlist.all()
    total_comments = Comments.objects.filter(listing=single_auction)
    comment_form = CommentForm(request.POST or None)
    if comment_form.is_valid():
        object = Comments(**comment_form.cleaned_data)
        object.created_by = request.user
        object.listing = single_auction
        object.save()
    bid_form = BidForm(request.POST or None)
    if bid_form.is_valid():
        bid_object = Bids(**bid_form.cleaned_data)
        bid_object.created_by = request.user
        bid_object.auction_listing = single_auction
        bid_object.save()
    context = {
        'auction': single_auction,
        'watchlist': watchlist,
        'comment_form': comment_form,
        'comments': total_comments,
        'bid_form': bid_form,
    }
    return render(request, 'auctions/single_auction_page.html',context)

@login_required
def add_to_watchlist(request, id):
    to_be_added = get_object_or_404(AuctionListing, id=id)
    request.user.watchlist.add(to_be_added)
    print(request.path_info)
    return redirect('/')


@login_required
def remove_from_watchlist(request, id):
    to_be_removed = get_object_or_404(AuctionListing, id=id)
    request.user.watchlist.remove(to_be_removed)
    print(request.path_info)
    return redirect('/')


@login_required
def watchlist_view(request):
    watchlist = request.user.watchlist.all()
    context = {
        'watchlist': watchlist,
    }
    return render(request, 'auctions/watchlist_view.html',context)


@login_required
def all_categories(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, "auctions/categories_list.html",context)


@login_required
def specific_category(request, id):
    category = Category.objects.get(id=id)
    auction_listing = AuctionListing.objects.filter(category=category)
    context = {
        'category': category,
        'auctions': auction_listing,
    }
    return render(request, 'auctions/single_category.html',context)

