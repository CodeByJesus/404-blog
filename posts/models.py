from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from tinymce.models import HTMLField # Importamos HTMLField

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = HTMLField() # Cambiamos a HTMLField
    fecha_creacion = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    is_pinned = models.BooleanField(default=False) # Nuevo campo para posts fijados
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='posts') # NUEVA LÍNEA: Relación con Category
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts') # NUEVA LÍNEA: Relación con Tag

    def __str__(self):
        return self.titulo

    def get_summary(self, num_words=30):
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(self.contenido, 'html.parser')
        # Eliminar todas las etiquetas de imagen antes de extraer el texto
        for img in soup.find_all('img'):
            img.decompose()
        text = soup.get_text() # Extrae todo el texto sin HTML
        words = text.split()
        return ' '.join(words[:num_words]) + ('...' if len(words) > num_words else '')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        permissions = [
            ("can_post", "Can post new articles"),
        ]

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author_name = models.CharField(max_length=80)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now) # Corregido a DateTimeField
    approved_comment = models.BooleanField(default=False) # Corregido el nombre del campo

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return f'Comment by {self.author_name} on {self.post.titulo[:50]}...'
    

class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='post_images/')
    caption = models.CharField(max_length=255, blank=True) # Opcional: para descripción de la imagen

    def __str__(self):
        return f"Image for {self.post.titulo}"