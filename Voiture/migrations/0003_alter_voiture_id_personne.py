# Generated by Django 4.2.10 on 2024-04-11 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Personne", "0002_personne"),
        ("Voiture", "0002_voiture_id_personne"),
    ]

    operations = [
        migrations.AlterField(
            model_name="voiture",
            name="id_personne",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="Personne.personne"
            ),
        ),
    ]
