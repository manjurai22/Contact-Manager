from django.shortcuts import render, redirect
from contact_app.models import Contact
from django.http import HttpResponseRedirect
from contact_app.forms import ProjectForm

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
    if request.method=="GET":
        form = ProjectForm()
        return render(request,"add_contact.html",{'form':form})
    else:
        form=ProjectForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            return redirect("contact-list")
    
# def edit_contact(request,pk):
#     if request.method=="GET":
#         contact=Contact.objects.get(pk=pk)
#         return render(request,'edit_contact.html',{"contact":contact},)
#     else:
#         contact=Contact.objects.get(pk=pk)
#         contact.contact=request.POST["name"]
#         contact.save()
#         return redirect('contact-list')

def edit_contact(request, pk):
    contact = Contact.objects.get(pk=pk)

    if request.method == "POST":
        form = ProjectForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact-list')
    else:
        form = ProjectForm(instance=contact)

    return render(request, 'edit_contact.html', {'form': form})