# Generated by Django 4.1.7 on 2023-05-22 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("alumno", "0007_alter_alumno_apellido"),
    ]

    operations = [
        migrations.AddField(
            model_name="alumno",
            name="pepe",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
