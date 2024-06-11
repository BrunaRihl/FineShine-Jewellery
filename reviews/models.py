from django.db import models

# Create your models here.
from django.core.validators import MinLengthValidator
from django.db import models

from django.contrib.auth.models import User
from products.models import Product


class Review(models.Model):
    """
    Represents a review for a product written by a user.
    Attr:
        product (Product): The product being reviewed.
        user (User): The user who wrote the review.
        title (str): The title of the review.
        text (str): The text content of the review.
        rating (int): The rating given by the user (from 1 to 5).
        created_at (datetime): The date and time when the review was created.
        updated_at (datetime): The date and time when the review was last updated.
    """

    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User, null=False, blank=False, on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    text = models.TextField(
        validators=[
            MinLengthValidator(50, "Review must be greater than 50 characters")
        ],
        max_length=400,
    )
    rating = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [["product", "user"]]
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
