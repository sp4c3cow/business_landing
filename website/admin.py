from django.contrib import admin
from .models import ContactForm

class AdminContact(admin.ModelAdmin):
    list_display = ['name', 'email', 'date']

admin.site.register(ContactForm, AdminContact)