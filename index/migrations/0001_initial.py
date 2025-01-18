# Generated by Django 5.1.4 on 2025-01-09 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=64)),
                ('course_des', models.TextField()),
                ('course_price', models.FloatField()),
                ('course_photo', models.ImageField(upload_to='')),
            ],
        ),
    ]
