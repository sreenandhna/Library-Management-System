# Generated by Django 4.2.5 on 2024-03-17 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0017_alter_issuedbook_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuedbook',
            name='book',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='newapp.newbookmodel'),
        ),
    ]
