from django.contrib import admin
from cursos.models import Materia, MateriaAdmin, Alumno, AlumnoAdmin
#Registramos nuestras clases principales.

admin.site.register(Materia, MateriaAdmin)
admin.site.register(Alumno, AlumnoAdmin)