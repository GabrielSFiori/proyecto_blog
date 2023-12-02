from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Category(models.Model):
    COLOR_CHOICES = (
        ('red', 'Rojo'),
        ('blue', 'Azul'),
        ('green', 'Verde'),
        ('yellow', 'Amarillo'),
        # Agrega más opciones según sea necesario
    )

    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    color = models.CharField(max_length=20, choices=COLOR_CHOICES)

    def __str__(self):
        return f'{self.name} ({self.description})'

    def save(self, *args, **kwargs):
        # Generar el slug automáticamente a partir del name
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class User(models.Model):
    # campos para users, usuario, email, bio, profile_picture, agregar otros de ser necesario.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=150)
    email = models.EmailField()
    bio = models.CharField(max_length=150)
    profile_picture = models.ImageField(
        upload_to='static/blog_personal/img/user', null=True, blank=True)

    def __str__(self):
        return f'{self.user}  - {self.email}'


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Borrador'),
        ('published', 'Publicado'),
        ('removed', 'Eliminado'),
    )

    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category, through="PostCategory")
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='draft')
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(
        upload_to='static/blog_personal/img/post', null=True, blank=True)
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Generar el slug automáticamente a partir del título
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.title} ({self.content})'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.post.title + " - " + self.category.name
