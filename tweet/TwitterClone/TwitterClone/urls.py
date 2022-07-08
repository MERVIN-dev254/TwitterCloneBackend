from rest_framework import routers
from django.contrib import admin
from Tweets import views
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'tweets', views.TweetViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
