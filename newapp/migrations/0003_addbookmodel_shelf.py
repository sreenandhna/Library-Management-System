# Generated by Django 5.0.3 on 2024-03-15 11:55

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0002_addbookmodel_alter_adminsignupmodel_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='addbookmodel',
            name='shelf',
            field=models.FloatField(),
            preserve_default=False,
        ),
    ]