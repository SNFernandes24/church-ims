# Generated by Django 3.2.4 on 2021-06-26 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['full_name']},
        ),
        migrations.RemoveField(
            model_name='profile',
            name='slug',
        ),
    ]
