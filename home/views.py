from django.shortcuts import render

from django.contrib import messages
from wishlist.models import Wishlist
from profiles.models import UserProfile

# Create your views here.

def index(request):
    """ A view to return the index page """

    if request.user.is_authenticated:
        user = UserProfile.objects.get(user=request.user)
        wishlist_items = Wishlist.objects.filter(user=user)

        product_names = ", ".join([ wishlist_item.product.name for wishlist_item in wishlist_items ])

        if product_names:
            messages.info(request, f"{product_names} is included in your wishlist. Compre ja!!! Compre, compre compre. Dedao Botini de qualidade")

    return render(request, 'home/index.html')