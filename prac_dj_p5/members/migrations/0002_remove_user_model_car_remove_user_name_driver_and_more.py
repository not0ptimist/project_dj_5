# Generated by Django 4.0.1 on 2022-02-22 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='model_car',
        ),
        migrations.RemoveField(
            model_name='user',
            name='name_driver',
        ),
        migrations.DeleteModel(
            name='Car',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
