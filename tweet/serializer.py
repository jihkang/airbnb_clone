from rest_framework import serializers
from .models import Tweet
from config.settings import AUTH_USER_MODEL

class TweetSerializer(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(queryset=AUTH_USER_MODEL)
    likes_count = serializers.IntegerField(read_only=True)
    class Meta:
        model = Tweet
        fields = ("id", "user", "content"   , "likes_count")
