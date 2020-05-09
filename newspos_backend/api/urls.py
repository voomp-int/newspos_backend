from django.urls import include, path
from . import views

urlpatterns = [
    path('welcome', views.welcome),
    path('getArticles', views.get_articles),
    path('addArticle', views.add_article),
    path('updateArticle/<int:article_id>', views.alter_article),
    path('deleteArticle/<int:article_id>', views.delete_article)
]
