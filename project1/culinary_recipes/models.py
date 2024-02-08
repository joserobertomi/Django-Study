from django.db import models

# Create your models here.


class Recipe(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=32)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=32)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipe/covers/%Y/%m/%d/')
