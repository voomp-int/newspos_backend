from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
import requests
from rest_framework import status
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# API Key from NewsAPI
apiKey = 'ae90a4873e4c412abf7a403efc46c1e7'

# Test API for newsapi service
@api_view(["GET"])
def welcome(request):
    content = {"message": "Welcome to the NewsApi!"}
    return JsonResponse(content)

# API calling
@api_view(["GET"])
def get_newsapi(request):
    resp = requests.get(
        'https://newsapi.org/v2/top-headlines?country=in&apiKey=' + apiKey)
    if resp.status_code != 200:
        return JsonResponse({'error': 'Something went wrong {}'.format(resp.status_code)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    articles = resp.json()['articles']
    response = []
    for article in articles:
        hope = {
            'source': article['source']['name'],
            'author': article['author'],
            'title': article['title'],
            'description': article['description'],
            'url': article['url'],
            'urlToImage': article['urlToImage'],
            'publishedAt': article['publishedAt'],
            'isPositive': isPositive(article['description'])
        }
        response.append(hope)

    return JsonResponse({'articles': response}, safe=False, status=status.HTTP_200_OK)


# Helper function to analyze sentiment
def isPositive(text_string):
    sid = SentimentIntensityAnalyzer()
    scores = sid.polarity_scores(text_string)
    if(scores['compound'] >= 0):
        return True
    else:
        return False
