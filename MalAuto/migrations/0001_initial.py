# Generated by Django 4.1.5 on 2023-04-08 14:11

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('images', models.ImageField(upload_to='clients')),
                ('data', models.DateField(default=datetime.datetime.now)),
                ('content', models.TextField(validators=[django.core.validators.MinLengthValidator(10)])),
            ],
        ),
    ]