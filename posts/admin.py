from django.contrib import admin
from django import forms # Importamos forms
from .models import Post, Comment, Image, Category, Tag # Importamos Image, Category, Tag
from tinymce.widgets import TinyMCE # Importamos TinyMCE
from tinymce.models import HTMLField # Importamos HTMLField

# Definimos el inline para las imágenes
class ImageInline(admin.StackedInline):
    model = Image
    extra = 1 # Muestra un campo extra para añadir una nueva imagen

# Definimos el ModelAdmin para Post
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_creacion', 'is_pinned', 'category') # Añadido category
    list_filter = ('is_pinned', 'fecha_creacion', 'autor', 'category', 'tags') # Añadido is_pinned, category, tags
    fields = ('titulo', 'contenido', 'autor', 'category', 'tags', 'is_pinned', 'fecha_creacion') # Añadido category, tags y ordenado
    inlines = [ImageInline] # Añadimos el inline de imágenes aquí
    filter_horizontal = ('tags',) # NUEVA LÍNEA: Para una mejor selección de etiquetas
    # Añadimos la sobreescritura del campo para usar TinyMCE
    formfield_overrides = {
        HTMLField: {'widget': TinyMCE},
    }

    class Media:
        js = (
            # '/static/tinymce/tinymce.min.js', # Gestionado por TINYMCE_JS_URL en settings.py
        )

# Registramos el modelo Post con nuestro PostAdmin personalizado
admin.site.register(Post, PostAdmin)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'text', 'post', 'created_date', 'approved_comment')
    list_filter = ('approved_comment', 'created_date')
    search_fields = ('author_name', 'text')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved_comment=True)
        self.message_user(request, "Selected comments have been successfully approved.")
    approve_comments.short_description = "Approve selected comments"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
