from django.db import models
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    id = models.AutoField(primary_key=True)
    source = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=300)
    description = models.TextField()
    content = models.TextField()
    url = models.CharField(max_length=350)
    urlToImage = models.TextField()
    publishedAt = models.DateTimeField()
    compound_score = models.FloatField()

    class Meta:
        db_table = "articles"

    def __str__(self):
        return self.title
