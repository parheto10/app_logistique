# Generated by Django 3.2.8 on 2022-07-25 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestions', '0002_remove_projet_employe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employer',
            name='contact',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employer',
            name='matricule',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]