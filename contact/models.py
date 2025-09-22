from django.db import models


class ContactInfo(models.Model):
    whatsapp_number = models.CharField(max_length=20, blank=True, null=True)
    linkedin_url = models.URLField(max_length=255, blank=True, null=True)
    x_url = models.URLField(max_length=255, blank=True, null=True)
    github_url = models.URLField(max_length=255, blank=True, null=True)
    telegram_url = models.URLField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    instagram_url = models.URLField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Contact Info ({self.email or 'No email'})"
