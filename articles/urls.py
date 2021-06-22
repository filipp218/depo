from django.urls import path

from . import views

urlpatterns = [
    path("", views.ArticleList.as_view()),
    path("article/<int:pk>", views.DetailArticleView.as_view()),
    path("article/add", views.ArticleCreateView.as_view()),
    path("category/<int:pk>", views.ArticleByCategory.as_view()),
    path("category/add", views.CategoryCreate.as_view()),
    path("feedback", views.FeedbackView.as_view()),
]
