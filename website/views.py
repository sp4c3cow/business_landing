from django.shortcuts import render
from .models import ContactForm

def index(request):
    return render(request, 'html/index.html')

def porftfolio_details(request):
    return render(request, 'html/portfolio-details.html')

def inner_page(request):
    return render(request, 'html/inner-page.html')

def contact_form(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact = ContactForm(name=name, email=email, subject=subject, message=message)
        contact.save()

        return render(request, 'html/thankyou.html')
    else:
        return render(request, 'html/index.html')