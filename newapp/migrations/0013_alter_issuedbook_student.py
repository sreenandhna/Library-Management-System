# Generated by Django 4.2.5 on 2024-03-17 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0012_issuedbook_book_alter_issuedbook_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuedbook',
            name='student',
            field=models.CharField(default=None, max_length=250),
        ),
    ]
