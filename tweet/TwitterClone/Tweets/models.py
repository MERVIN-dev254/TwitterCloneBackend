from django.db import models

# Create your models here.
class Tweet(models.Model):
    tweet_text = models.TextField()
    tweet_img = models.ImageField(upload_to='uploads/tweet-images',
                                  null=True, blank=True)
    
    def __str__(self) -> str:
        return self.tweet_text
    
class Reply(models.Model):
    tweet = models.ForeignKey(to=Tweet, on_delete=models.CASCADE)
    reply_text = models.TextField()
    reply_img = models.ImageField(upload_to='uploads/tweet-images/replies', 
                                  null = True, blank=True)
    

