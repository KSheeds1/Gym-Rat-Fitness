from django.db import models
from django.contrib.auth.models import User
from profiles.models import UserProfile


class Post(models.Model):
    """ Fields necessary for a post """

    class Meta:
        ordering = ['-posted_on']

    user_profile = models.ForeignKey(UserProfile,
                                     on_delete=models.CASCADE,
                                     related_name='posts',
                                     null=True, blank=True)
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(default='', null=True,
                              blank=True)
    image_url = models.URLField(max_length=1024, null=True,
                                blank=True)
    posted_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description


class Comments(models.Model):
    """ Fields necessary to comment on a post """

    class Meta:
        verbose_name_plural = 'Comments'

    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='details')
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    comment_date = models.DateTimeField(auto_now=True)


class Like(models.Model):
    """ Fields necessary to like a post """
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='likes')
