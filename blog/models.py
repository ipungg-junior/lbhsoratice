from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    img = models.ImageField()
    content = models.TextField()

    def __str__(self):
          return self.title
  
    def get_absolute_url(self):
          return reverse('blog:post_detail', args=[self.slug])