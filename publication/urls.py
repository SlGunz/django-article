from django.urls import include, path
from . import views

urlpatterns = [
    path('all/', views.ArticleListView.as_view(), name='index'),
    path('<int:pk>/', views.article_detail, name='article-detail'),
]
