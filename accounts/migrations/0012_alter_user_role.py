# Generated by Django 4.2.4 on 2023-09-08 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_rename_locaion_userprofile_location_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.PositiveBigIntegerField(blank=True, choices=[(2, 'Customer'), (1, 'Vendor')], null=True),
        ),
    ]
