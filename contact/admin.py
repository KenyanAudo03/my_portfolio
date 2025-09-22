from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import ContactInfo


class SingleContactInfoForm(ModelForm):
    def clean(self):
        if ContactInfo.objects.exists() and not self.instance.pk:
            raise ValidationError("Only one ContactInfo instance is allowed.")
        return super().clean()


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    form = SingleContactInfoForm
    list_display = ("email", "whatsapp_number", "linkedin_url", "github_url")
    search_fields = ("email", "whatsapp_number")
