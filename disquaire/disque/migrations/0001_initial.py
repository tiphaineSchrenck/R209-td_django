# Generated by Django 4.0.3 on 2022-05-06 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disquaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('ville', models.CharField(max_length=100)),
                ('cp', models.IntegerField()),
                ('nom_rue', models.CharField(max_length=100)),
                ('num_rue', models.IntegerField()),
                ('num_tel', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Disque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('label', models.CharField(max_length=100)),
                ('artiste', models.CharField(max_length=100)),
                ('date_sortie', models.DateField(blank=True, null=True)),
                ('nb_morceaux', models.IntegerField()),
                ('duree', models.IntegerField(blank=True)),
                ('magasin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='disque.disquaire')),
            ],
        ),
    ]
