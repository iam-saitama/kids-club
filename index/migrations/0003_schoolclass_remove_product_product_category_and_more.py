# Generated by Django 5.1.4 on 2025-01-17 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_category_product_delete_courses'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=50)),
                ('class_schedule', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
