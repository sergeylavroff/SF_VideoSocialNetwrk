from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class VSNUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    nickname = models.CharField(max_length=50)
    pic = models.ImageField(blank=True, upload_to='media/')
    
    def __str__(self):
        return self.nickname

class Video(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=2048)
    preview = models.ImageField(blank=True, upload_to='media/')
    author = models.ForeignKey(VSNUser, on_delete=models.CASCADE, related_name='video_author')
    likes = models.ManyToManyField(VSNUser, related_name='video_likers')
    dislikes = models.ManyToManyField(VSNUser, related_name='video_dislikers')

class Comment(models.Model):
    author = models.ForeignKey(VSNUser,on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    text = models.TextField(max_length=2048)
    likes = models.ManyToManyField(VSNUser, related_name='comment_likers')
    dislikes = models.ManyToManyField(VSNUser, related_name='comment_dislikers')

class Channel(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=2048)
    owner = models.ForeignKey(VSNUser,on_delete=models.CASCADE, related_name='channel_owner')
    subscribers = models.ManyToManyField(VSNUser, related_name='channel_subscribers')
    ignorers = models.ManyToManyField(VSNUser, related_name='channel_ignorers')