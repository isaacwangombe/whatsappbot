# Generated by Django 4.0.2 on 2023-09-13 07:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('storechatbot', '0013_profiles_email_profiles_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartment',
            name='renter',
        ),
        migrations.AddField(
            model_name='apartment',
            name='occupied',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='profiles',
            name='apartment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='storechatbot.apartment'),
        ),
        migrations.AlterField(
            model_name='profiles',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
