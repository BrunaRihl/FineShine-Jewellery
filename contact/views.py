from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm

def index(request):
    """ A view to return contact page and submit contact form """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()

            # Prepare email variables
            subject = f"New Contact Form Submission from {contact.name}"
            message = f"Name: {contact.name}\nEmail: {contact.email}\nPhone: {contact.phone}\n\nMessage:\n{contact.message}"

            # Send email
            send_mail(subject, message, 'brunarihl@gmail.com', ['brunarihl@gmail.com'])

            return redirect('success')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def success_page(request):
    """ A view to return contact success page """
    return render(request, 'contact_success.html')
