from django import forms
from django.contrib import admin
from .models import Contact
import re


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'contact_number']

        widgets = {
            'contact_number': forms.TextInput(attrs={
                'maxlength': '19',
                'data-mask': '+998 (00) 000-00-00',  # Маска для JavaScript
            }),
            'name': forms.TextInput(attrs={
                'placeholder': 'Введите ваше имя',
            }),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        # Проверяем, что имя содержит только буквы и пробелы
        if not re.match(r'^[a-zA-Zа-яА-Я\s]+$', name):
            raise forms.ValidationError("Имя должно содержать только буквы и пробелы.")
        return name

    def clean_contact_number(self):
        contact_number = self.cleaned_data.get('contact_number')

        # Удаляем все нечисловые символы
        sanitized_number = re.sub(r'\D', '', contact_number)

        # Проверяем длину и формат
        if not sanitized_number.startswith('998') or len(sanitized_number) != 12:
            raise forms.ValidationError("Неверный формат номера. Пожалуйста, используйте формат +998(xx)xxx-xx-xx.")

        # Форматируем номер в виде +998(xx)xxx-xx-xx
        formatted_number = f"+{sanitized_number[:3]}({sanitized_number[3:5]}){sanitized_number[5:8]}-{sanitized_number[8:10]}-{sanitized_number[10:12]}"

        return formatted_number