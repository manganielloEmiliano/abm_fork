# Generated by Django 4.1.7 on 2023-05-22 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profesor", "0004_alter_profesor_apellido"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profesor",
            name="apellido",
            field=models.CharField(max_length=50, verbose_name="Apellidirigillio"),
        ),
    ]
