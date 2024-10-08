# Generated by Django 4.2.4 on 2023-09-08 02:23

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_userprofile_latitude_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='locaion',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.PositiveBigIntegerField(blank=True, choices=[(2, 'Customer'), (1, 'Vendor')], null=True),
        ),
    ]
