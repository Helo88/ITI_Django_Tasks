# Generated by Django 4.0.1 on 2022-02-03 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('affairs', '0005_students_confirm_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='confirm_password',
        ),
    ]