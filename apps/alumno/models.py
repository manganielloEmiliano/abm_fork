from django.db import models

from apps.utils.models import Persona


class Alumno(Persona):
    monotributo = models.BooleanField(default=False, null=True)

    def __str__(self):
        algo4 = super().__str__()
        return f'Alumno: {algo4}'
