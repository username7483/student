# Generated by Django 4.2.6 on 2023-10-05 14:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marshall', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='teacher',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='students_taught', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterModelTable(
            name='attendance',
            table='attendance',
        ),
        migrations.AlterModelTable(
            name='attendancereport',
            table='attendancereport',
        ),
        migrations.AlterModelTable(
            name='notificationstaffs',
            table='notificationstaffs',
        ),
        migrations.AlterModelTable(
            name='notificationstudent',
            table='notificationstudent',
        ),
        migrations.AlterModelTable(
            name='sessionyearmodel',
            table='sessionyearmodel',
        ),
        migrations.AlterModelTable(
            name='studentresult',
            table='studentresult',
        ),
        migrations.AlterModelTable(
            name='students',
            table='students',
        ),
        migrations.AlterModelTable(
            name='teacher',
            table='teacher',
        ),
    ]