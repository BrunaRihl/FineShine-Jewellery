from django import forms


class ReviewForm(forms.Form):
    """
    Form for creating or editing a review.
    Attr:
        title (CharField): The title of the review.
        rating (IntegerField): The rating given by the user (from 1 to 5).
        text (CharField): The text content of the review.
    """

    title = forms.CharField(max_length=200)
    rating = forms.IntegerField(min_value=1, max_value=5)
    text = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, block_fields=False, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        if block_fields:
            for field in self.fields:
                self.fields[field].widget.attrs["readonly"] = True

        for field_name, field in self.fields.items():
            field.widget.attrs["placeholder"] = f"{field_name} here ..."
