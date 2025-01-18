from django.db import models

# Create your models here.


# Занятия
class SchoolClass(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name}'


# Выбор дня недели
class ClassSchedule(models.Model):
    # Generate time choices for every hour from 00:00 to 23:00
    HOUR_CHOICES = [(i, f"{str(i).zfill(2)}") for i in range(24)]

    # Choices for minutes (0 to 59)
    MINUTE_CHOICES = [(i, f"{str(i).zfill(2)}") for i in range(0, 60, 5)]  # Every 5 minutes

    hour = models.IntegerField(
        choices=HOUR_CHOICES,
        default=0,
    )
    minute = models.IntegerField(
        choices=MINUTE_CHOICES,
        default=0,
    )

    DAYS_OF_WEEK = [
        ('Понедельник', 'Понедельник'),
        ('Вторник', 'Вторник'),
        ('Среда', 'Среда'),
        ('Четверг', 'Четверг'),
        ('Пятница', 'Пятница'),
        ('Суббота', 'Суббота'),
        ('Воскресенье', 'Воскресенье'),
    ]

    school_class = models.ForeignKey(SchoolClass, related_name='schedules', on_delete=models.CASCADE)
    day_of_week = models.CharField(
        max_length=11,
        choices=DAYS_OF_WEEK,
    )
    def __str__(self):
        return f"{self.school_class.name} - {self.hour}:{self.minute:02d} on {self.day_of_week}"


# Телефон школы
class SchoolNumber(models.Model):
    name = models.CharField(max_length=100)
    school_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name


# Заявка клиента
class Contact(models.Model):
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.contact_number})"
