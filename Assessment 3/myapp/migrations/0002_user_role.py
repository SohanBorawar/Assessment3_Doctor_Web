# Generated by Django 4.2.4 on 2023-08-10 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(default='patient', max_length=100),
        ),
    ]
