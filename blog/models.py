from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    content = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
          return self.title
  
    def get_absolute_url(self):
          return reverse('blog:post_detail', args=[self.slug])