# Generated by Django 3.0.4 on 2020-04-16 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacApp', '0014_auto_20200415_2215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adrequest',
            name='rank_1',
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateField(),
        ),
    ]
