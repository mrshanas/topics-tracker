# Generated by Django 4.0 on 2021-12-11 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0002_entry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='body',
        ),
    ]
