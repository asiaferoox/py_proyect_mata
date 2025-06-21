from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField


class Post(models.Model):
    titulo    = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    contenido = RichTextField()
    imagen    = models.ImageField(upload_to='posts/', null=True, blank=True)
    fecha     = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class Comment(models.Model):
    post    = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author  = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body    = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.titulo}'
