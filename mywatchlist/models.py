from django.db import models

# Create your models here.


class MyWatchList(models.Model):
    watched = models.BooleanField()
    title = models.CharField(max_length=120)
    rating = models.FloatField()
    release_date = models.CharField(max_length=120)
    review = models.TextField()
