# Generated by Django 5.1.5 on 2025-02-20 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0002_alter_citymodel_city_name_weathermodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weathermodel',
            name='city',
            field=models.CharField(max_length=50),
        ),
    ]
