from django.db import models
from django.utils import timezone

class Post(models.Model):
    """ Blog post class definition.
    """
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        """ Publish blog post.
        """
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        """ Override __str__.
        """
        return self.title
