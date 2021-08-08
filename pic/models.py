from django.db import models
from django.contrib.auth.models import User


class Picture(models.Model):
    name = models.CharField(max_length=30, default="picture")
    pictures = models.ImageField()

    def __str__(self):
        return self.name

class Sub(models.Model): # This is a separate model or table created for the requested user inorder to store his/her SMASHES and to avoid repetition in the model or table of Picture in the database which could lead to excessive repetition of pictures that are displayed
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sub", null=True)
    sub_name = models.CharField(max_length=30, default="picture")
    sub_pictures = models.ImageField()

    def __str__(self):
        return self.sub_name


# Create your models here.
