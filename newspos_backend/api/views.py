from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view
from .serializers import ArticleSerializer
from .models import Article
from rest_framework import status
import json
from rest_framework.response import Response
from rest_framework.pagination import CursorPagination
from rest_framework import generics


@api_view(["GET"])
def welcome(request):
    content = {"message": "Welcome to our shit!"}
    return JsonResponse(content)


@api_view(["GET"])
def get_articles(request):
    articles = Article.objects.all()

    # Paginator Specific
    paginator = CursorPagination()
    paginator.ordering = "id"
    result_page = paginator.paginate_queryset(articles, request)
    next_page = paginator.get_next_link()
    previous_page = paginator.get_previous_link()
    count = paginator.get_page_size(request)

    serializer = ArticleSerializer(result_page, many=True)
    return JsonResponse(
        {
            "count": count,
            "previous": previous_page,
            "next": next_page,
            "articles": serializer.data,
        },
        status=status.HTTP_200_OK,
    )


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
            publishedAt=payload["publishedAt"],
        )
        serializer = ArticleSerializer(article)
        return JsonResponse(
            {"article": serializer.data}, status=status.HTTP_201_CREATED
        )
    except ObjectDoesNotExist as e:
        return JsonResponse({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse(
            {"error": "Something went wrong"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["PUT"])
def alter_article(request, article_id):
    payload = json.loads(request.body)
    try:
        article_item = Article.objects.filter(id=article_id)
        article_item.update(**payload)
        article = Article.objects.get(id=article_id)
        serializer = ArticleSerializer(article)
        return JsonResponse({"article": serializer.data}, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse(
            {"error": "Something went wrong"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["DELETE"])
def delete_article(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse(
            {"error": "Something went wrong"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
