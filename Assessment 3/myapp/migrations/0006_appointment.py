# Generated by Django 4.2.4 on 2023-08-20 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_patient_age_patient_profile_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(upload_to='appointment_user/')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.PositiveIntegerField()),
                ('doctor_field', models.CharField(max_length=100)),
                ('doctor', models.CharField(max_length=100)),
                ('appointment_time', models.DateTimeField()),
                ('date_time', models.DateTimeField()),
                ('appointment_request', models.BooleanField(default=False)),
                ('Doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.patient')),
            ],
        ),
    ]
