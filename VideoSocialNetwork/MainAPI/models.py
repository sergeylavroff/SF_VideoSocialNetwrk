from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class VSNUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    nickname = models.CharField(max_length=50)
    pic = models.ImageField(blank=True, upload_to='media/')

    class Meta:
      verbose_name_plural = "users"
    
    def __str__(self):
        return self.nickname

class Channel(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=2048)
    owner = models.ForeignKey(VSNUser,on_delete=models.CASCADE, related_name='channel_owner')
    subscribers = models.ManyToManyField(VSNUser, related_name='channel_subscribers', blank=True)
    ignorers = models.ManyToManyField(VSNUser, related_name='channel_ignorers', blank=True)

    class Meta:
      verbose_name_plural = "channels"

    def __str__(self):
        return self.name

class Video(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=2048)
    preview = models.ImageField(blank=True, upload_to='media/')
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name='video_channel')
    likes = models.ManyToManyField(VSNUser, related_name='video_likers', blank=True)
    dislikes = models.ManyToManyField(VSNUser, related_name='video_dislikers', blank=True)
    content = models.FileField(blank=True, upload_to='media/')

    class Meta:
      verbose_name_plural = "videos"

    def __str__(self):
        return self.name

class Comment(models.Model):
    author = models.ForeignKey(VSNUser,on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    text = models.TextField(max_length=2048)
    likes = models.ManyToManyField(VSNUser, related_name='comment_likers', blank=True)
    dislikes = models.ManyToManyField(VSNUser, related_name='comment_dislikers', blank=True)

    class Meta:
      verbose_name_plural = "comments"

    def __str__(self):
        return self.text
