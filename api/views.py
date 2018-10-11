from rest_framework import generics
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib import auth
from publication import models
from . import serializers


class ArticleList(generics.ListAPIView):
    """
    Provides a list of all articles.
    """
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer


class ArticleDetail(mixins.RetrieveModelMixin,
                    generics.GenericAPIView):
    """
    Retreieve an article item.
    """
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ArticleCommentsList(APIView):
    """
    Provides a list of all comments for the article.
    """
    def get_object(self, pk):
        try:
            return models.Article.objects.get(pk=pk)
        except models.Article.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        article = self.get_object(pk)
        comments = models.Comment.objects.filter(article=article)
        serializer = serializers.CommentSerializer(comments, many=True)
        return Response(serializer.data)


class UserDetail(mixins.RetrieveModelMixin,
                 generics.GenericAPIView):
    """
    Retrieve a user item.
    """
    queryset = auth.get_user_model().objects.all()
    serializer_class = serializers.UserSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
