# Generated by Django 4.0.3 on 2022-05-08 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disque', '0008_disquaire_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='disque',
            name='genre',
            field=models.CharField(choices=[('ENVOYEE', 'Envoyée'), ('VALIDEE', 'Validée'), ('DEMANDEE', 'Demandée')], default='ENVOYEE', max_length=15, verbose_name='Statut'),
        ),
    ]
