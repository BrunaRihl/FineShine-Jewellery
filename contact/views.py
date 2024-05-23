from django.shortcuts import render, redirect
from .forms import ContactForm


def index(request):
    """ A view to return contact page and submit contact form """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def success_page(request):
    """ A view to return contact success page """

    return render(request, 'contact_success.html')