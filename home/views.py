from datetime import datetime
import pytz

from django.conf import settings
from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse
from django.utils.safestring import mark_safe

from profiles.models import UserProfile
from wishlist.models import Wishlist


def index(request):
    """
    A view to return the index page.

    If the user is authenticated, check for expired items
    in the user's wishlist and display a message with a link
    to the wishlist if there are any.
    """

    if request.user.is_authenticated:
        user = UserProfile.objects.get(user=request.user)
        # Get the timezone configured in Django
        timezone = pytz.timezone(settings.TIME_ZONE)

        # Get the current datetime and make it "aware"
        now = datetime.now(timezone)
        wishlist_items = Wishlist.objects.filter(
            user=user, reminder_date__lte=now
        )

        product_names = ", ".join(
            [wishlist_item.product.name for wishlist_item in wishlist_items]
        )

        if product_names:
            # Customize the message with a link to the wishlist
            wishlist_url = reverse(
                "view_wishlist"
            )  # Get the URL of the wishlist
            message = mark_safe(
                f"Still interested in {product_names}? "
                f"It's waiting for you on your wishlist! "
                f"<a href='{wishlist_url}' class='wishlistt-link'>Go to Wishlist</a>"
            )
            messages.info(request, message)

    return render(request, "home/index.html")
