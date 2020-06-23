from django.contrib import admin
from .models import *

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    fieldsets = (('Datos', {'fields': ('nombre', 'ejemplares')}) , ('Contacto', {'fields': ('telefono', 'direccion')}), )


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ['titulo' , 'editorial']

@admin.register(Ejemplar)
class EjemplarAdmin(admin.ModelAdmin):
    list_display = ['libro', 'localizacion']
    list_display_links = ( 'localizacion', 'libro')
    search_fields = ['libro__titulo']

class LibroInline(admin.TabularInline):
    model = Libro
    fields = ['titulo', 'editorial', 'paginas']

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ['nombre',]
    list_display_links = ('nombre',)
    search_fields = ['nombre']
    inlines = [LibroInline]
    
    

# Register your models here.