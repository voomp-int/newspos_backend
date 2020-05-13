from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
import requests
from rest_framework import status

# API Key from NewsAPI
apiKey = 'ae90a4873e4c412abf7a403efc46c1e7'

# Test API for newsapi service
@api_view(["GET"])
def welcome(request):
    content = {"message": "Welcome to the NewsApi!"}
    return JsonResponse(content)


@api_view(["GET"])
def get_newsapi(request):
    resp = requests.get(
        'https://newsapi.org/v2/top-headlines?country=in&apiKey=' + apiKey)
    if resp.status_code != 200:
        return JsonResponse({'error': 'Something went wrong {}'.format(resp.status_code)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return JsonResponse({'response': resp.json()}, safe=False, status=status.HTTP_200_OK)
