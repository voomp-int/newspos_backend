from django.urls import include, path
from . import views

urlpatterns = [
    path('welcome', views.welcome),
    path('getArticles', views.get_articles),
]
