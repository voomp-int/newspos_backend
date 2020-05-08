from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializers import ArticleSerializer
from .models import Article
from rest_framework import status


@api_view(["GET"])
def welcome(request):
    content = {"message": "Welcome to our shit!"}
    return JsonResponse(content)


@api_view(["GET"])
def get_articles(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return JsonResponse({'articles': serializer.data}, status=status.HTTP_200_OK)
