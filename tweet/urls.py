from django.urls import path
from . import views


urlpatterns = [
    path("", views.index),
    path("api/v1/tweets", views.TweetsView.as_view()),
    path("api/v1/users/<str:username>/tweets", views.UserTweetsView.as_view()),
]