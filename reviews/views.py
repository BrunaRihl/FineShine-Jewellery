from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from profiles.models import UserProfile

from .models import Review
from products.models import Product

from .forms import ReviewForm


@login_required
def create_review(request, item_id):
    """
    """ 
    product = get_object_or_404(Product, pk=item_id)
    user = UserProfile.objects.get(user=request.user)
    orders = user.orders.all()

    request_user = request.user

    if not orders:
        messages.error(
            request, "You must have purchased this product to review it."
        )
        return redirect("product_detail", item_id)

    product_purchased = False
    for order in orders:
        for item in order.lineitems.all():
            if item.product == product:
                product_purchased = True
                break

    if not product_purchased:
        messages.error(
            request, "You must have purchased this product to review it."
        )
        return redirect("product_detail", item_id)

    review_exists = Review.objects.filter(
        product=product, user=request_user
    ).exists()

    if review_exists:
        messages.error(request, "You have already reviewed this product")
        return redirect("product_detail", item_id)

    form = ReviewForm()

    if request.method == "POST":
        title = request.POST["title"]
        text = request.POST["text"]
        rating = request.POST["rating"] or 0
        review = Review(
            product=product,
            user=request_user,
            title=title,
            text=text,
            rating=rating,
        )
        review.save()

        messages.success(request, "Your review has been added.")
        return redirect("product_detail", item_id)

    context = {
        "product": product,
        "form": form,
    }

    return render(request, "create_review.html", context)


@login_required
def edit_review(request, review_id):
    """
    """
    review = get_object_or_404(Review, id=review_id, user=request.user)
    product = review.product
    form = ReviewForm(
        initial={
            "title": review.title,
            "text": review.text,
            "rating": review.rating,
        }
    )

    if request.method == "POST":
        title = request.POST["title"]
        text = request.POST["text"]
        rating = request.POST["rating"]
        review.title = title
        review.text = text
        review.rating = rating
        review.save()

        messages.success(request, "Your review has been updated.")
        return redirect("product_detail", product.id)

    context = {
        "product": product,
        "form": form,
        "review": review,
    }

    return render(request, "edit_review.html", context)


@login_required
def delete_review(request, review_id):
    """
    """
    review = get_object_or_404(Review, id=review_id, user=request.user)
    product = review.product

    if request.method == "GET":
        form = ReviewForm(
            initial={
                "title": review.title,
                "text": review.text,
                "rating": review.rating,
            },
            block_fields=True,
        )
        context = {
            "product": product,
            "form": form,
            "review": review,
        }

        return render(request, "delete_review.html", context)

    if request.method == "POST":
        review.delete()

        messages.success(request, "Your review has been deleted.")
        return redirect("product_detail", product.id)