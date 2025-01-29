from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count
from .models import Tweet


def index(request):
    tweets = Tweet.objects.annotate(likes_count=Count("liked_by")).order_by("-likes_count")
    # return HttpResponse(output)

    return render(request, "index.html", {"tweets": tweets})
