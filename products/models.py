from django.db import models


class Category(models.Model):
    """
    A model representing a product category.
    Attr:
        name (str): The name of the category.
        friendly_name (str): A human-friendly name for the category, which can be null or blank.
    """

    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        """
        Return the string representation of the category, which is its name.
        """
        return self.name

    def get_friendly_name(self):
        """
        Return the friendly name of the category.
        """
        return self.friendly_name


class Product(models.Model):
    """
    A model representing a product.
    """

    category = models.ForeignKey(
        "Category", null=True, blank=True, on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        """
        Return the string representation of the product, which is its name.
        """
        return self.name
