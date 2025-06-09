from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
        # This method returns the URL to access the detail view of the post.
        # It uses Django's reverse function to generate the URL based on the 'post-detail' 
        # view and the primary key of the post.


    def __str__(self):
        return self.title


