# Generated by Django 3.1.4 on 2020-12-04 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0005_auto_20201204_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_ref',
            field=models.CharField(editable=False, max_length=32, primary_key=True, serialize=False),
        ),
    ]
