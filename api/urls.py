from django.urls import path 
from . import views

urlpatterns = [
     path('articles/', views.ArticleList.as_view()),
     path('article/<int:pk>/', views.ArticleDetail.as_view()),
     path('comments/<int:pk>/', views.ArticleCommentsList.as_view()),
     path('user/<int:pk>/', views.UserDetail.as_view()),
]
