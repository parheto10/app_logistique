# Generated by Django 3.2.8 on 2022-07-21 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parametres', '0003_alter_fonction_libelle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fonction',
            name='libelle',
            field=models.CharField(max_length=225, unique=True),
        ),
    ]