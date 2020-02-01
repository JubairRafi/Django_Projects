from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User #make relationship between user.and for that we need forien key
from django.urls import reverse

# Create your models here.

#creating class/table for users as post model

class post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title #for printing info as title// post object 1 as blog 1

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk' : self.pk})