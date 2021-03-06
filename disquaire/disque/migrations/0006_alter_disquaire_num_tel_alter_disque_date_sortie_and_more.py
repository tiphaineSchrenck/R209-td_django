# Generated by Django 4.0.3 on 2022-05-06 17:06

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('disque', '0005_alter_disque_date_sortie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disquaire',
            name='num_tel',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
        migrations.AlterField(
            model_name='disque',
            name='date_sortie',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='disque',
            name='duree',
            field=models.DurationField(verbose_name='MM: SS'),
        ),
    ]
