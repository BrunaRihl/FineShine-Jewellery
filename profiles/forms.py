from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """
    Form for updating user profile information.
    This form is used to update the user profile information, excluding the user field.
    It customizes field attributes such as placeholders, classes, and autofocus on the first field.
    Attr:
        model (UserProfile): The UserProfile model used for the form.
        exclude (tuple): Fields to exclude from the form.
    """

    class Meta:
        model = UserProfile
        exclude = ("user",)

    def __init__(self, *args, **kwargs):
        """
        Initialize the form and customize field attributes.
        This method sets placeholders, classes, and autofocus on the first field.
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            "default_phone_number": "Phone Number",
            "default_postcode": "Postal Code",
            "default_town_or_city": "Town or City",
            "default_street_address1": "Street Address 1",
            "default_street_address2": "Street Address 2",
            "default_county": "County, State or Locality",
        }

        self.fields["default_phone_number"].widget.attrs["autofocus"] = True
        for field in self.fields:
            if field != "default_country":
                if self.fields[field].required:
                    placeholder = f"{placeholders[field]} *"
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs["placeholder"] = placeholder
            self.fields[field].widget.attrs[
                "class"
            ] = "border-black rounded-0 profile-form-input"
            self.fields[field].label = False
