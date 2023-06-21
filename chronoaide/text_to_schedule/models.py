from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length = 255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()