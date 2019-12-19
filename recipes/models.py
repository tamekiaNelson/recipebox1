from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Recipe(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    instructions = models.TextField()
    post_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title} - {self.author.name}"
