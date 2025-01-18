from django import forms
from .models import ClassSchedule
from .models import Contact, SchoolNumber

class ClassScheduleForm(forms.ModelForm):
    class Meta:
        model = ClassSchedule
        fields = ['school_class', 'hour', 'minute', 'day_of_week']

    # Override the widgets for hour and minute
    hour = forms.ChoiceField(
        choices=ClassSchedule.HOUR_CHOICES,
        widget=forms.Select,
    )
    minute = forms.ChoiceField(
        choices=ClassSchedule.MINUTE_CHOICES,
        widget=forms.Select,
    )

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