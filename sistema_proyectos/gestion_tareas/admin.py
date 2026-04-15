from django.contrib import admin
from .models import Proyecto, Tarea

class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'usuario', 'creado_en')
    search_fields = ('nombre',)
    list_filter = ('creado_en',)

class TareaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'proyecto', 'completada', 'creado_en')
    search_fields = ('titulo',)
    list_filter = ('completada', 'proyecto')

admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(Tarea, TareaAdmin)