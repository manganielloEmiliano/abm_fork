# Generated by Django 4.2.5 on 2023-09-23 01:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alumno', '0009_alter_alumno_pepe'),
        ('examen', '0002_examenalumno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examenalumno',
            name='alumno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alumno', to='alumno.alumno'),
        ),
        migrations.AlterField(
            model_name='examenalumno',
            name='examen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='examen', to='examen.examen'),
        ),
    ]
