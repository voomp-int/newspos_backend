from django.db import models
from django.utils import timezone

# Create your models here.


class Article(models.Model):
    source = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    url = models.CharField(max_length=250)
    urlToImage = models.CharField(max_length=250)
    publishedAt = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
