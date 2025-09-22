from .models import ContactInfo


def contact_info(request):
    contact = ContactInfo.objects.first()
    return {"contact_info": contact}
