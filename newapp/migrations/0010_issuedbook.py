# Generated by Django 5.0.3 on 2024-03-16 08:15

import newapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0009_studentsignupmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='IssuedBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('bookname', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=30)),
                ('issuedate', models.DateField(auto_now=True)),
                ('expirydate', models.DateField(default=newapp.models.get_expiry)),
            ],
        ),
    ]
