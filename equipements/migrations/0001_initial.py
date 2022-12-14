# Generated by Django 3.2.8 on 2022-07-25 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('parametres', '0005_auto_20220722_0936'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accessoires',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=255, unique=True)),
                ('date_achat', models.DateField()),
                ('prix_achat', models.IntegerField(blank=True, null=True)),
                ('quantity', models.IntegerField(default=0)),
                ('destination', models.CharField(max_length=255)),
                ('qty_today', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Materiels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=255, null=True)),
                ('num_serie', models.CharField(blank=True, max_length=255, null=True)),
                ('model', models.CharField(max_length=255)),
                ('marque', models.CharField(max_length=255)),
                ('etat', models.CharField(choices=[('FONCTIONNELLE', 'FONCTIONNELLE'), ('ENDOMMAGE', 'ENDOMMAGE'), ('REPARATION', 'REPARATION')], default='', max_length=255)),
                ('date_achat', models.DateField()),
                ('quantity', models.IntegerField(default=0)),
                ('prix_achat', models.IntegerField(blank=True, null=True)),
                ('materiel_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('type_materiel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parametres.type_materiel')),
            ],
        ),
    ]
