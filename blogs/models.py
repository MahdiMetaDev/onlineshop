from django.db import models
from django.urls import reverse


class Blog(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    content = models.TextField()
    cover = models.ImageField(upload_to='covers/', default='covers/default_cover.jpg')
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', args=[self.pk])
