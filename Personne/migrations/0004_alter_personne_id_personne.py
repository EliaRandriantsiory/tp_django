# Generated by Django 4.2.10 on 2024-04-15 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Personne", "0003_delete_personnemodels"),
    ]

    operations = [
        migrations.AlterField(
            model_name="personne",
            name="id_personne",
            field=models.AutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
    ]
