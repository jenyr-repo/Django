# Generated by Django 5.1.1 on 2024-10-06 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('contact', models.CharField(max_length=300, verbose_name='Phone_number')),
                ('time', models.TimeField()),
                ('count', models.IntegerField()),
                ('notes', models.CharField(blank=True, max_length=300)),
            ],
        ),
    ]
