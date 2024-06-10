import datetime
from django.db import models

from profiles.models import UserProfile
from products.models import Product
import pytz
from django.conf import settings


def get_default_reminder_date():
    timezone = pytz.timezone(settings.TIME_ZONE)
    now = datetime.datetime.now(timezone)
    return now + datetime.timedelta(days=5)

class Wishlist(models.Model):
    """
    Represents a wishlist item linking a user to a desired product.
    Attributes:
        user (ForeignKey): A reference to the user profile associated with the wishlist.
        product (ForeignKey): A reference to the product that the user wishes for.
        is_favorite (BooleanField): Indicates whether the item is marked as a favorite by the user.
        created_at (DateTimeField): The timestamp when the wishlist item was created.
        reminder_date (DateTimeField): The date set for reminding the user about the wishlist item.
    """


    user = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="user_wishlist",
    )

    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE
    )

    is_favorite = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    reminder_date = models.DateTimeField(
        default=get_default_reminder_date
    )

    class Meta:
        unique_together = ("user", "product")
        verbose_name = "Wishlist Item"
        verbose_name_plural = "Wishlist Items"

    def __str__(self):
        return f"Wishlist item of {self.user.user.username}: {self.product.name}"
