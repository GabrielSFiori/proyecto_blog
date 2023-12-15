from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone
from accounts.models import UserModel


class Category(models.Model):
    COLOR_CHOICES = (
        ('red', 'Red'),
        ('orange', 'Orange'),
        ('yellow', 'Yellow'),
        ('olive', 'Olive'),
        ('green', 'Green'),
        ('teal', 'Teal'),
        ('blue', 'Blue'),
        ('violet', 'Violet'),
        ('purple', 'Purple'),
        ('pink', 'Pink'),
        ('brown', 'Brown'),
        ('grey', 'Grey'),
        ('black', 'Black'),
    )

    name = models.CharField(max_length=50)
    description = models.TextField()
    slug = models.SlugField(null=False, blank=False, unique=True)
    color = models.CharField(
        max_length=20, choices=COLOR_CHOICES, default='celeste')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', "DRAFT"),
        ('published', "PUBLISHED"),
        ('removed', "REMOVED"),
    )

    title = models.CharField(max_length=150, null=False)
    content = models.TextField()
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    categories = models.ManyToManyField(Category, through='PostCategory')
    status = models.CharField(choices=STATUS_CHOICES,
                              default='DRAFT', max_length=20)
    slug = models.SlugField(null=False, blank=False, unique=True)
    image = models.ImageField(upload_to="image", null=True, blank=True)
    author = models.ForeignKey(
        'accounts.UserModel', on_delete=models.CASCADE)

    comments_count = models.IntegerField(default=0)
    views_count = models.IntegerField(default=0)
    likes_count = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='posts')

    class Meta:
        unique_together = ('post', 'category')

    def __str__(self):
        return self.post.title + " - " + self.category.name


class Comment(models.Model):
    author = models.ForeignKey(
        'accounts.UserModel', on_delete=models.CASCADE)
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    comment_post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    likes_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.author} - {self.comment_post.title}"
