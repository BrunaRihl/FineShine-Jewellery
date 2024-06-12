from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    A form for creating and updating Contact instances.
    This form includes fields for name, email, phone, and message.
    It uses the Contact model to define the fields and sets
    custom placeholders for each field.
    """

    class Meta:
        model = Contact
        fields = ["name", "email", "phone", "message"]

    def __init__(self, *args, **kwargs):
        """
        Initialize the form and set custom placeholders for each field.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            "name": "Full Name",
            "email": "Email Address",
            "phone": "Your phone number",
            "message": "Please provide details about your inquiry...",
        }

        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs["placeholder"] = placeholder
