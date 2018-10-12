from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


def get_default_creator():
    return get_user_model().objects.get_or_create(username='default-publicator')[0]


class Article(models.Model):
    """
    Model represents an article.
    """
    title = models.CharField(max_length=200)
    preview_image = models.URLField(max_length=200, null=True)
    content = RichTextUploadingField()
    pub_date = models.DateField(auto_now=True)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET(get_default_creator))

    @property
    def breif(self):
        """
        Return the brief content of the article
        """
        return self.content[:200]

    def __str__(self):
        """
        Create a string for the Article.
        """
        return self.title

    def get_absolute_url(self):
        """
        Return the url to access a particular book instance.
        """
        return reverse("article-detail", args=[str(self.id)])


class Comment(models.Model):
    """"
    Model represent a user comment to an article.
    """
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE)
    message = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.DO_NOTHING)

    def __str__(self):
        """
        Create a string for the Comment.
        """
        return self.message[:100]

    def get_absolute_url(self):
        """
        Return the url of an article that the comment belongs.
        """
        return reverse("article", args=[str(article.id)])
