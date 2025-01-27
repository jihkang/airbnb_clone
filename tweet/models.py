from django.db import models
from users.models import CustomUser
from config import settings


class CustomModel(models.Model):
    """ custom model """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
    

class Like(CustomModel):
    """ like model """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='likes'
    )
    tweet = models.ForeignKey(
        'Tweet',
        on_delete=models.CASCADE,
        related_name='likes_set'
    )

    class Meta:
        unique_together = (("user", "tweet"))

# Create your models here.
class Tweet(CustomModel):
    """ tweet model """
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="tweets")
    content = models.TextField(max_length=100)
    liked_by = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='Like',
        related_name='liked_tweets'
    )

    def likes_count(self):
        return self.liked_by.count()

    def __str__(self):
        return f"{self.content}"