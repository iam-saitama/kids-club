from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.db.models import Prefetch
from .models import ClassName, ClassSchedule, SchoolNumber
from .forms import ContactForm


# Create your views here.
# Главная страница
def home(request):
    # Получаем все занятия и их расписания
    classes = ClassName.objects.prefetch_related(
        Prefetch('schedule', queryset=ClassSchedule.objects.all(), to_attr='schedules')
    )

    # Получаем номер школы
    school_number = SchoolNumber.objects.first()

    # Рендерим шаблон с контекстом
    return render(request, 'home.html', {
        'classes': classes,
        'school_number': school_number,
    })


# Оставить заявку
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Заявка успешно отправлена!")
            return redirect(f"{reverse('home')}#contact")  # Перенаправление с якорем
        else:
            # Сохраняем ошибки формы в сообщениях
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{form.fields[field].label}: {error}")
            return redirect(f"{reverse('home')}#contact")  # Перенаправление с якорем
    else:
        form = ContactForm()

    # Загружаем шаблон главной страницы с формой
    return render(request, 'home.html', {'form': form})