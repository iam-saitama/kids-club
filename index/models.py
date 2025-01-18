from django.db import models

# Create your models here.

# Занятия
class SchoolClass(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=50)
    class_schedule = models.TextField()

    def __str__(self):
        return self.name


# Телефон школы
class SchoolNumber(models.Model):
    name = models.CharField(max_length=255, default="Unknown")
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.phone_number


# Заявка клиента
class Contact(models.Model):
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.contact_number})"
