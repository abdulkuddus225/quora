# Generated by Django 2.2.6 on 2020-02-29 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quora_clone', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='answers',
        ),
    ]
