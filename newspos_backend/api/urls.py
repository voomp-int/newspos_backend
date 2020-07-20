from django.urls import include, path
from . import views

urlpatterns = [
    path("welcome", views.welcome),
    path("articles", views.get_articles),
    path("articles", views.add_article),
    path("articles/<int:article_id>", views.alter_article),
    path("articles/<int:article_id>", views.delete_article),
]
