# Generated by Django 3.0.3 on 2020-04-27 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainweb', '0002_auto_20200427_0758'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='title',
        ),
    ]
