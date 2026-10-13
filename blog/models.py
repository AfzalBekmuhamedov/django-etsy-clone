from django.contrib.auth.models import AbstractUser
from django.db import models
from django.template.defaultfilters import title

from config.settings import AUTH_USER_MODEL


class User(AbstractUser):
    address = models.TextField(blank=True,null=True)

class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"

class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to="images/")
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comment(models.Model):
    title = models.TextField()
    user = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE)
    article = models.ForeignKey(Product,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
