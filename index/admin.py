from django.contrib import admin
from .models import SchoolClass, SchoolNumber
from .models import Contact
from django import forms

# Create a custom form for the admin interface
class SchoolAdminForm(forms.ModelForm):
    class Meta:
        model = SchoolNumber
        fields = ['name', 'phone_number']

# Register the model with the admin interface
class SchoolAdmin(admin.ModelAdmin):
    form = SchoolAdminForm

admin.site.register(SchoolNumber, SchoolAdmin)


# Register your models here.
admin.site.register(SchoolClass)
admin.site.register(Contact)