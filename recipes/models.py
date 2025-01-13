from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=65) #VARCHAR
    description = models.CharField(max_length=165)
    slug = models.SlugField() #slug
    preparation_time = models.IntegerField() #INT
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    serving_unit = models.CharField(max_length=65)
    preparation_step = models.TextField() #Tamanho livre
    preparation_step_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True) #auto_now_add faz com que no momento da criação pegue a data atual
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/', blank=True, default='')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, default=None,) # Caso a categoria for apagada torna o campo nulo, o null permite que o campo seja nulo
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, default=None)

    def __str__(self):
        return self.title
