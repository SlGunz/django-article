from django.db import models


class Picture(models.Model):
    """
    Model represent an image storage
    """
    title = models.CharField(max_length=100)
    picture = models.ImageField(upload_to="uploads/%Y/%m/%d/")
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
