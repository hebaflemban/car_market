# Generated by Django 2.2.13 on 2020-09-03 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_car_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]