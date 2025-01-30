from django.shortcuts import render
from django.db.models import Count
from config import settings
from .models import Tweet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TweetSerializer
from django.apps import apps
from django.db.models import QuerySet

def ordering_by_likes(tweets):
    if isinstance(tweets, QuerySet):
        return tweets.annotate(likes_count=Count("liked_by")).order_by("-likes_count")
    
    return tweets.objects.annotate(likes_count=Count("liked_by")).order_by("-likes_count")


def index(request):
    tweets = Tweet.objects.annotate(likes_count=Count("liked_by")).order_by("-likes_count")
    # return HttpResponse(output)

    return render(request, "index.html", {"tweets": tweets})


@api_view(["GET"])
def tweets(request):
    tweets = ordering_by_likes(Tweet)
    return Response({
        "success": True,
        "tweets": TweetSerializer(tweets, many=True).data,
    })


@api_view(["GET"])
def user_tweets(request, username: str):
    try:
        User = apps.get_model(settings.AUTH_USER_MODEL)
        user = User.objects.filter(username=username).first()
            
        if not User:
            raise User.DoesNotExist
    
        tweets = ordering_by_likes(Tweet.objects.filter(user=user))
        return Response({
                "success": True,
                "tweets": TweetSerializer(tweets, many=True).data,
            },
            status=200,
        )
    
    except User.DoesNotExist:
        return Response({"error": "user not found"}, status=404)