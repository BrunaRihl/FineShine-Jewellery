from django.urls import path
from . import views

urlpatterns = [
    path("", views.view_wishlist, name="view_wishlist"),
    path("add/<int:item_id>/", views.add_to_wishlist, name="add_to_wishlist"),
    path("remove/<int:item_id>/", views.remove_from_wishlist, name="remove_from_wishlist"),
    path("toggle_favorite/<int:item_id>/", views.toggle_favorite, name="toggle_favorite"),
]
