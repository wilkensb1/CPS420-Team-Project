# Generated by Django 4.1.13 on 2023-12-08 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_delivered'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='discount',
            field=models.CharField(default='0', max_length=10),
        ),
    ]
