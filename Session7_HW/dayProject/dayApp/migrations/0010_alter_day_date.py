# Generated by Django 4.0.3 on 2022-04-11 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dayApp', '0009_alter_day_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='date',
            field=models.DateField(),
        ),
    ]
