# Generated by Django 3.2.8 on 2022-08-01 10:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gestions', '0011_attribution_etat'),
    ]

    operations = [
        migrations.AddField(
            model_name='mission',
            name='date_terminer',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
