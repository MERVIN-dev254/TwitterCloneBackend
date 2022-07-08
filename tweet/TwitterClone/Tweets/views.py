from django.shortcuts import render
from rest_framework import viewsets
from Tweets.models import Tweet

from Tweets.serializers import TweetSerializer

# Create your views here.
class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    