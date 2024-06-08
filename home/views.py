from django.shortcuts import render

from django.contrib import messages
from wishlist.models import Wishlist
from profiles.models import UserProfile
from datetime import datetime
import pytz
from django.conf import settings

def index(request):
    """ A view to return the index page """

    if request.user.is_authenticated:
        user = UserProfile.objects.get(user=request.user)
        # Get the timezone configured in Django
        timezone = pytz.timezone(settings.TIME_ZONE)

        # Get the current datetime and make it "aware"
        now = datetime.now(timezone)
        wishlist_items = Wishlist.objects.filter(user=user, reminder_date__lte=now)

        product_names = ", ".join([wishlist_item.product.name for wishlist_item in wishlist_items])

        if product_names:
            messages.info(request, f"{product_names} is included in your wishlist. Buy now!!! Buy, buy, buy. Botini's top-notch deal!")

    return render(request, 'home/index.html')
