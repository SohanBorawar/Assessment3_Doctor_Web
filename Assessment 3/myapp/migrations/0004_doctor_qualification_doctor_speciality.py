# Generated by Django 4.2.4 on 2023-08-13 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_contact_doctor_patient_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='qualification',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='doctor',
            name='speciality',
            field=models.CharField(default='', max_length=100),
        ),
    ]