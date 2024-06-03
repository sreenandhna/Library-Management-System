# Generated by Django 5.0.3 on 2024-03-15 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0007_alter_newbookmodel_shelf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newbookmodel',
            name='shelf',
        ),
        migrations.AddField(
            model_name='newbookmodel',
            name='shelfid',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]
