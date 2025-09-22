from django.contrib import admin
from .models import ContactInfo


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ("email", "whatsapp_number", "linkedin_url", "github_url")
    search_fields = ("email", "whatsapp_number")
