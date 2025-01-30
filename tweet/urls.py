from django.urls import path
from . import views


urlpatterns = [
    path("", views.index),
    path("api/v1/tweets", views.tweets),
    path("api/v1/users/<str:username>/tweets", views.user_tweets),
]