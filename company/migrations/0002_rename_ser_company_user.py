# Generated by Django 5.1.4 on 2024-12-29 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='ser',
            new_name='user',
        ),
    ]
