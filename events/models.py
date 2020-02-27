from django.db import models
from django.contrib.auth.models import User
class Event(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    location = models.CharField(max_length = 60)
    datetime = models.DateTimeField()
    seats = models.PositiveIntegerField()
    owner = models.ForeignKey(User , on_delete= models.CASCADE)
