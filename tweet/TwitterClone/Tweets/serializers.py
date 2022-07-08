from dataclasses import fields
from rest_framework import serializers

from Tweets.models import Tweet

class TweetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tweet
        fields = '__all__'
        
