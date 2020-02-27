from django.db import models

class Event(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    location = models.CharField(max_length = 60)
    datetime = models.DateTimeField()
    seats = models.PositiveIntegerField()
