# Generated by Django 3.2 on 2023-09-05 02:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendor',
            old_name='is_approve',
            new_name='is_approved',
        ),
    ]
