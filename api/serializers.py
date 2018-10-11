from rest_framework import serializers
from publication import models
from django.contrib import auth


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'preview_image',
            'content',
            'pub_date',
            'creator',
        )

        model = models.Article


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'message',
            'pub_date',
            'owner',
        )

        model = models.Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
        )

        model = auth.get_user_model()
