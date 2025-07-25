from django import forms
from .models import Contact

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone', 'email']