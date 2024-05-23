from django.db import models

from django.db import models
from profiles.models import UserProfile
from products.models import Product


class Wishlist(models.Model):
    """
    Represents a wishlist item linking a user to a desired product.
    Attrs:
        user (ForeignKey): A reference to the user profile associated with the wishlist.
        product (ForeignKey): A reference to the product that the user wishes for.
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

    def __str__(self):
        return self.product.name