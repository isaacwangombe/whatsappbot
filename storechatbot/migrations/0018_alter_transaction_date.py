# Generated by Django 4.0.2 on 2023-09-26 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storechatbot', '0017_transaction_sender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
