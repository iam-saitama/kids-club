from django import forms
from .models import Contact, SchoolNumber

class PhoneNumberForm(forms.ModelForm):
    class Meta:
        model = SchoolNumber
        fields = ['school_number']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'contact_number']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ваше имя'}),
            'contact_number': forms.TextInput(attrs={'placeholder': 'Ваш телефон'}),
        }