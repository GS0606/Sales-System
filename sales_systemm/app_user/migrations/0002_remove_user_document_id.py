# Generated by Django 5.1.2 on 2024-11-08 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='document_id',
        ),
    ]