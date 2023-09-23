from django.contrib import admin

# Register your models here.
from apps.examen.models import Examen, ContenidoExamen, ExamenAlumno


@admin.register(Examen)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('materia', 'fecha')
    search_fields = ('materia',)
    list_filter = ('materia',)

@admin.register(ContenidoExamen)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('examen', 'titulo')
    search_fields = ('examen',)
    list_filter = ('examen',)

@admin.register(ExamenAlumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('alumno', 'examen')
    search_fields = ('alumno',)
    list_filter = ('alumno',)