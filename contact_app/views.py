from django.shortcuts import render
from contact_app.models import Contact

def contact_list(request):
    contacts=Contact.objects.all()
    return render(
        request,
        "contact_list.html",
        {"contacts":contacts},
    )
