# Generated by Django 3.2.8 on 2022-07-22 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('parametres', '0005_auto_20220722_0936'),
    ]

    operations = [
        migrations.CreateModel(
            name='Engins',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=225)),
                ('marque', models.CharField(max_length=225)),
                ('couleur', models.CharField(max_length=225)),
                ('matricule', models.CharField(max_length=225)),
                ('numcharsis', models.CharField(max_length=225)),
                ('date_achat', models.DateField()),
                ('mise_en_circulation', models.DateField()),
                ('prix_achat', models.IntegerField(blank=True, null=True)),
                ('etat', models.CharField(choices=[('DISPONIBLE', 'DISPONIBLE'), ('OCCUPE', 'OCCUPE'), ('VENDU', 'VENDU')], default='', max_length=100)),
                ('engin_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('type_engins', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parametres.type_vehicule')),
            ],
        ),
    ]