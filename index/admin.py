from django.db import models
from django.contrib import admin
from .models import SchoolNumber, Contact, ClassSchedule, ClassName


class ClassScheduleInline(admin.StackedInline):
    model = ClassSchedule
    extra = 1

class SchoolClassAdmin(admin.ModelAdmin):
    inlines = [ClassScheduleInline]

    def get_inline_instances(self, request, obj=None):
        if obj is None:  # Если объект новый (добавление)
            return []  # Не показываем связанные модели (расписание)
        return super().get_inline_instances(request, obj)


# Регистрация моделей в админке
admin.site.register(ClassName, SchoolClassAdmin)
admin.site.register(ClassSchedule)
admin.site.register(Contact)
admin.site.register(SchoolNumber)