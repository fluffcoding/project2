from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.auction_list_creation, name="create-auction"),
    path("auction/<id>/", views.single_auction_view, name="single-auction"),
    path("add-to-watchlist/<id>", views.add_to_watchlist, name='add-to-watchlist'),
    path("watchlist/", views.watchlist_view, name='watchlist'),
    path("remove-from-watchlist/<id>", views.remove_from_watchlist, name='remove-from-watchlist'),
    path("all-categories/", views.all_categories, name='categories'),
    path("category/<id>/", views.specific_category, name='single-category')

]
