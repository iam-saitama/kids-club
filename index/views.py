from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PhoneNumberForm
from .forms import ContactForm
from .models import SchoolClass, SchoolNumber


# Create your views here.
# Главная страница
def home(request):
    classes = SchoolClass.objects.all()
    return render(request, 'index/index.html',{'classes': classes})


# О нас
# def about(request):
#     classes = SchoolClass.objects.all()
#     return render(request, 'index/about.html', {'classes': classes})

def about(request):
    classes = SchoolClass.objects.all()
    school_number = SchoolNumber.objects.first()  # Get the first school instance (or adjust based on your logic)

    # If the form is submitted (POST request)
    if request.method == 'POST':
        form = PhoneNumberForm(request.POST, instance=school_number)
        if form.is_valid():
            form.save()
            return redirect('about')  # Redirect to about page after saving
    else:
        form = PhoneNumberForm(instance=school_number)  # Show form with existing data (if any)

    return render(request, 'index/about.html', {'classes': classes, 'form': form, 'school': school_number})


# Занятия
def school_classes(request):
    classes = SchoolClass.objects.all()
    return render(request, 'index/about.html', {'classes': classes})


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