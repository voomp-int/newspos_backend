from django.http import JsonResponse
from rest_framework.decorators import api_view


@api_view(["GET"])
def welcome(request):
    content = {"message": "Welcome to our shit!"}
    return JsonResponse(content)
