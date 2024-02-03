from django.db import models
import uuid

class Category(models.Model):
    title = models.CharField(max_length = 100)

    def __str__(self):
        return self.title

class Note(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    reminder = models.DateTimeField(False, False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
