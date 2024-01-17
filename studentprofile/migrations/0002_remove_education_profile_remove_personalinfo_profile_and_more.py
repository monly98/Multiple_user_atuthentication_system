# Generated by Django 5.0.1 on 2024-01-14 07:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentprofile', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='personalinfo',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='skills',
            name='profile',
        ),
        migrations.AddField(
            model_name='education',
            name='student',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='student',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='skills',
            name='student',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='student',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
