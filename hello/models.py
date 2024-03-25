from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Feedback(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
        
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def get_absolute_url(self):
        return reverse("landing")
    
    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title.lower()

class Subcategory(models.Model):
    title = models.CharField(max_length=100)
    parent_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title.lower()

class Recipe(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    
    image = models.ImageField(upload_to="recipe_images")
    
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def get_absolute_url(self):
        return reverse("recipe-detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.title
        

