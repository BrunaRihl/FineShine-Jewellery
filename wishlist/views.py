from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from products.models import Product
from .models import Wishlist
from profiles.models import UserProfile
from django.http import HttpResponse


@login_required
def view_wishlist(request):
    """
    Display the user's wishlist.
    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered 'wishlist.html' template with wishlist items.
    """
    user = UserProfile.objects.get(user=request.user)
    wishlist_items = Wishlist.objects.filter(user=user)

    return render(request, "wishlist.html", {"wishlist_items": wishlist_items})

@login_required
def add_to_wishlist(request, item_id):
    """
    Add a product to the user's wishlist.
    Args:
        request (HttpRequest): The request object.
        item_id (int): ID of the product to add.
    """
    product = get_object_or_404(Product, pk=item_id)
    user = UserProfile.objects.get(user=request.user)

    if Wishlist.objects.filter(user=user, product=product).exists():
        messages.warning(request, f"{product.name} is already included in your wishlist.")
    else:
        Wishlist.objects.create(user=user, product=product)
        messages.success(request, f"Successfully added {product.name} to your wishlist!")

    return redirect(reverse("product_detail", args=[item_id]))

@login_required
def remove_from_wishlist(request, item_id):
    """
    Remove a product from the user's wishlist.
    Args:
        request (HttpRequest): The request object.
        item_id (int): ID of the product to remove.
    """
    product = get_object_or_404(Product, pk=item_id)
    user = UserProfile.objects.get(user=request.user)
    wishlist_item = Wishlist.objects.get(user=user, product=product)

    wishlist_item.delete()
    messages.success(request, f"{product.name} has been removed from wishlist.")
    return redirect(reverse("view_wishlist"))