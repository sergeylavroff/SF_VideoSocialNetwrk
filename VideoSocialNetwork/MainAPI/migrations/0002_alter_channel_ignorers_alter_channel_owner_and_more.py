# Generated by Django 4.0.4 on 2022-06-04 11:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MainAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='ignorers',
            field=models.ManyToManyField(related_name='channel_ignorers', to='MainAPI.vsnuser'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='channel_owner', to='MainAPI.vsnuser'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='subscribers',
            field=models.ManyToManyField(related_name='channel_subscribers', to='MainAPI.vsnuser'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='dislikes',
            field=models.ManyToManyField(related_name='comment_dislikers', to='MainAPI.vsnuser'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='likes',
            field=models.ManyToManyField(related_name='comment_likers', to='MainAPI.vsnuser'),
        ),
        migrations.AlterField(
            model_name='video',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video_author', to='MainAPI.vsnuser'),
        ),
        migrations.AlterField(
            model_name='video',
            name='dislikes',
            field=models.ManyToManyField(related_name='video_dislikers', to='MainAPI.vsnuser'),
        ),
        migrations.AlterField(
            model_name='video',
            name='likes',
            field=models.ManyToManyField(related_name='video_likers', to='MainAPI.vsnuser'),
        ),
        migrations.AlterField(
            model_name='vsnuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
