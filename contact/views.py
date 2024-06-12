from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactForm


def index(request):
    """
    Display the contact page and handle form submission.

    If the request method is POST, validate and save the contact form,
    then send an email notification. If an error occurs during email
    sending, display an error message.
    """
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                contact = form.save()

                # Prepare email variables
                subject = f"New Contact Form Submission from {contact.name}"
                message = (
                    f"Name: {contact.name}\n"
                    f"Email: {contact.email}\n"
                    f"Phone: {contact.phone}\n\n"
                    f"Message:\n{contact.message}"
                )

                # Send email
                send_mail(
                    subject,
                    message,
                    "fineshine@example.com",
                    ["brunarihl@gmail.com"],
                )

                return redirect("success")
            
            except Exception as e:
                # Log the error or handle it accordingly
                print(f"Error sending email: {e}")
                return render(
                    request,
                    "contact.html",
                    {
                        "form": form,
                        "error": "There was an error sending your message. "
                                "Please try again later.",
        },
    )

    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})


def success_page(request):
    """
    Display the contact form success page.
    """
    return render(request, "contact_success.html")
