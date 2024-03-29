from typing import Iterable
from django.db import models
from django.utils.text import slugify

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.full_name()


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption

class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.TextField()
    image = models.ImageField(default=None, upload_to="posts_image")
    date = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True, max_length=120, blank=True, db_index=True)
    content = models.TextField()
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL, related_name="posts")
    tags = models.ManyToManyField(Tag, related_name="posts", blank=True)


    def save(self, *args, **kwargs):
        if(not self.slug):
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

