# Generated by Django 4.0.4 on 2022-07-26 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainAPI', '0004_remove_video_author_video_channel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='ignorers',
            field=models.ManyToManyField(blank=True, related_name='channel_ignorers', to='MainAPI.vsnuser'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='subscribers',
            field=models.ManyToManyField(blank=True, related_name='channel_subscribers', to='MainAPI.vsnuser'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='dislikes',
            field=models.ManyToManyField(blank=True, related_name='comment_dislikers', to='MainAPI.vsnuser'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='comment_likers', to='MainAPI.vsnuser'),
        ),
        migrations.AlterField(
            model_name='video',
            name='dislikes',
            field=models.ManyToManyField(blank=True, related_name='video_dislikers', to='MainAPI.vsnuser'),
        ),
        migrations.AlterField(
            model_name='video',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='video_likers', to='MainAPI.vsnuser'),
        ),
    ]