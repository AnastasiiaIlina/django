from django.db import models
import uuid

class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length = 100)
    description = models.TextField()
    reminder = models.DateTimeField(False, False)
    category = models.CharField(max_length = 100)

    def __str__(self):
        return self.title

class User(models.Model):
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

