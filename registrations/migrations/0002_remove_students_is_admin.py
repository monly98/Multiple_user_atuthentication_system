# Generated by Django 5.0.1 on 2024-01-09 04:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='is_admin',
        ),
    ]