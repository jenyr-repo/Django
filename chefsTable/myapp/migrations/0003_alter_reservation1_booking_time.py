# Generated by Django 5.1.1 on 2024-10-07 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_reservation1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation1',
            name='booking_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
