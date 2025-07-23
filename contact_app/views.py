from django.shortcuts import render
from contact_app.models import Contact
from django.http import HttpResponseRedirect

def contact_list(request):
    contacts=Contact.objects.all()
    return render(
        request,
        "contact_list.html",
        {"contacts":contacts},
    )

def delete_contact(request,pk):
    contact=Contact.objects.get(pk=pk)
    contact.delete()
    return HttpResponseRedirect("/")

def add_contact(request):
    print(request.method,request.POST)
    if request.method=="GET":
        return render(request,"")
    else:
        Contact.objects.add(name=request.POST["name"])
        return HttpResponseRedirect("/")
    
def edit_contact(request,pk):
    if request.method=="GET":
        contact=Contact.objects.get(pk=pk)
        return render(request,"",{"contact":contact},)
    else:
        contact=Contact.objects.get(pk=pk)
        contact.contact=request.POST["name"]
        contact.save()
        return HttpResponseRedirect("/")