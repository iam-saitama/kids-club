# Generated by Django 5.1.4 on 2025-01-18 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_rename_phone_number_schoolnumber_school_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schoolclass',
            name='class_schedule',
        ),
        migrations.AddField(
            model_name='schoolclass',
            name='day_of_week',
            field=models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], default='Monday', max_length=9),
        ),
        migrations.AddField(
            model_name='schoolclass',
            name='time',
            field=models.TimeField(default='12:00:00'),
        ),
        migrations.AlterField(
            model_name='schoolclass',
            name='age',
            field=models.PositiveIntegerField(),
        ),
    ]
