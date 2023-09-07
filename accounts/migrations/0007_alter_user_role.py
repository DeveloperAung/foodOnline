# Generated by Django 4.2.4 on 2023-09-07 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.PositiveBigIntegerField(blank=True, choices=[(2, 'Customer'), (1, 'Vendor')], null=True),
        ),
    ]
