from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view
from .serializers import ArticleSerializer
from .models import Article
from rest_framework import status
import json


@api_view(["GET"])
def welcome(request):
    content = {"message": "Welcome to our shit!"}
    return JsonResponse(content)


@api_view(["GET"])
def get_articles(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return JsonResponse({'articles': serializer.data}, status=status.HTTP_200_OK)


@api_view(["POST"])
def add_article(request):
    payload = json.loads(request.body)
    try:
        article = Article.objects.create(
            source=payload["source"],
            author=payload["author"],
            title=payload["title"],
            description=payload["description"],
            url=payload["url"],
            urlToImage=payload["urlToImage"],
            publishedAt=payload["publishedAt"]
        )
        serializer = ArticleSerializer(article)
        return JsonResponse({'article': serializer.data}, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
