from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            "id",
            "source",
            "author",
            "title",
            "description",
            "content",
            "compound_score",
            "url",
            "urlToImage",
            "publishedAt",
        ]
