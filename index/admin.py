from django.db import models
from django.contrib import admin
from .models import SchoolClass, SchoolNumber, ClassSchedule
from .models import Contact
from django import forms
from .forms import ClassScheduleForm

# Create a custom form for the admin interface
# Inline model for adding multiple schedules to each class
class ClassScheduleInline(admin.TabularInline):
    model = ClassSchedule
    extra = 1  # Shows one empty row for adding new schedules


class SchoolClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')
    inlines = [ClassScheduleInline]


class ClassScheduleAdmin(admin.ModelAdmin):
    form = ClassScheduleForm
    list_display = ['school_class', 'hour', 'minute', 'day_of_week']


# Generate time choices for every hour from 00:00 to 23:00
TIME_CHOICES = [(f"{str(i).zfill(2)}:00", f"{str(i).zfill(2)}:00") for i in range(24)]

class ClassScheduleForm(forms.ModelForm):
    class Meta:
        model = ClassSchedule
        fields = '__all__'

    # Override the time field to use a ChoiceField with predefined time options
    time = forms.ChoiceField(
        choices=TIME_CHOICES,
        widget=forms.Select,
    )
#
# # Register the model with the admin interface
# class SchoolClassAdmin(admin.ModelAdmin):
#     # Fields to display in the admin list view
#     list_display = ('name', 'age', 'day_of_week', 'time')
#
#     # Add filtering by day_of_week in the list view
#     list_filter = ('day_of_week',)
#
#     # Add a search field to search by name
#     search_fields = ('name',)
#
#     # Add a custom form layout for better structure
#     fieldsets = (
#         (None, {
#             'fields': ('name', 'age', 'day_of_week', 'time')
#         }),
#     )

    # Configure the form to use a dropdown for `day_of_week` and `time` picker for `time`
    formfield_overrides = {
        models.CharField: {'widget': admin.widgets.AdminTextInputWidget()},
        models.TimeField: {'widget': admin.widgets.AdminTimeWidget()},
    }


# Register your models here.
admin.site.register(ClassSchedule, ClassScheduleAdmin)
admin.site.register(SchoolClass, SchoolClassAdmin)
admin.site.register(SchoolNumber)
admin.site.register(Contact)