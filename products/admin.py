from django.contrib import admin
from .models import Product, Category

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    """
    Administration interface customization for Product model.
    This class customizes the administration interface for Product model,
    specifying the list display fields and ordering.
    """

    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    """
    Administration interface customization for Category model.
    This class customizes the administration interface for Category model,
    specifying the list display fields.
    """
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)