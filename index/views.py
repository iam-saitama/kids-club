from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PhoneNumberForm
from .forms import ContactForm
from .models import SchoolClass, SchoolNumber


# Create your views here.
# Главная страница
def home(request):
    classes = SchoolClass.objects.all()
    school_number = SchoolNumber.objects.get(pk=1)
    return render(request, 'index/index.html',{'classes': classes, 'school_number': school_number})


# О нас
def about(request):
    try:
        school_number = SchoolNumber.objects.get(pk=1)  # Adjust this to your actual query
    except SchoolNumber.DoesNotExist:
        school_number = None  # If no entry exists

    return render(request, 'index/about.html', {'school_number': school_number})


# Занятия
def school_classes(request):
    classes = SchoolClass.objects.all()
    return render(request, 'index/classes.html', {'classes': classes})


# Оставить заявку
def contact(request):
    classes = SchoolClass.objects.all()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Заявка успешно отправлена!")
            return redirect('contact')
        else:
            messages.error(request, "В вашей заявке была ошибка.")
    else:
        form = ContactForm()

    return render(request, 'index/contact.html', {'form': form, 'classes': classes})