from django.db import models

# Create your models here.

# Название занятия/урока
class ClassName(models.Model):
    name = models.CharField("Название занятия", max_length=100)
    age = models.PositiveIntegerField("Возраст")

    def __str__(self):
        return f"{self.name} (Возраст от {self.age} лет)"

    class Meta:
        verbose_name = "Занятие"
        verbose_name_plural = "Занятия"


class ClassSchedule(models.Model):
    # Выбор дня недели и времени
    DAYS_OF_WEEK = [
        ('Понедельник', 'Понедельник'),
        ('Вторник', 'Вторник'),
        ('Среда', 'Среда'),
        ('Четверг', 'Четверг'),
        ('Пятница', 'Пятница'),
        ('Суббота', 'Суббота'),
        ('Воскресенье', 'Воскресенье'),
    ]

    HOUR_CHOICES = [(i, f'{i:02}') for i in range(7, 21)]  # Часы с 7 до 20
    MINUTE_CHOICES = [(i, f'{i:02}') for i in range(0, 60, 15)]  # Каждые 15 минут

    school_class = models.ForeignKey(
        'ClassName',
        related_name='schedule',
        on_delete=models.CASCADE,
        verbose_name="Занятие"
    )
    day_of_week = models.CharField("День недели", max_length=20, choices=DAYS_OF_WEEK)
    hour = models.PositiveIntegerField("Час", choices=HOUR_CHOICES)
    minute = models.PositiveIntegerField("Минута", choices=MINUTE_CHOICES)

    class Meta:
        verbose_name = "Расписание занятий"
        verbose_name_plural = "Расписание занятий"
        unique_together = ['school_class', 'day_of_week', 'hour', 'minute']
        ordering = ['day_of_week', 'hour', 'minute']

    def __str__(self):
        return f"{self.school_class.name} - {self.day_of_week} - {self.formatted_time()}"

    def formatted_time(self):
        # Возвращает строку в формате 'HH:MM'
        return f"{str(self.hour).zfill(2)}:{str(self.minute).zfill(2)}"

    def clean(self):
        # Валидация расписания на уникальность
        from django.core.exceptions import ValidationError
        if ClassSchedule.objects.filter(
            school_class=self.school_class,
            day_of_week=self.day_of_week,
            hour=self.hour,
            minute=self.minute
        ).exists():
            raise ValidationError("Это время уже занято для данного занятия и дня недели.")


# Телефон школы
class SchoolNumber(models.Model):
    name = models.CharField("Название школы", max_length=100)
    school_number = models.CharField("Номер школы", max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Телефон школы"
        verbose_name_plural = "Телефон школы"

# Заявка клиента
class Contact(models.Model):
    name = models.CharField("Имя", max_length=100)
    contact_number = models.CharField("Номер телефона", max_length=19, help_text="Format: +998(xx)xxx-xx-xx")
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    def save(self, *args, **kwargs):
        # Добавляем +998
        if not self.contact_number.startswith('+998'):
            self.contact_number = '+998' + self.contact_number
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.contact_number})"

    class Meta:
        verbose_name = "Заявка клиента"
        verbose_name_plural = "Заявки клиентов"