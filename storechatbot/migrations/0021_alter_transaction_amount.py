# Generated by Django 4.0.2 on 2023-09-27 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storechatbot', '0020_apartment_balance_apartment_payment_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
