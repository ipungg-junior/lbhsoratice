from django.db import models
from django.urls import reverse
from django.utils import timezone

class Tag(models.Model):
    nametag = models.CharField(max_length=12)

    def __str__(self):
          return self.nametag

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to='article-banner', default='default.jpg')
    slug = models.SlugField(max_length=200)
    content = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    tag = models.ManyToManyField(Tag, null=True, blank=True)
    visitor = models.IntegerField(default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
          return self.title
  
    def get_absolute_url(self):
          return reverse('blog:post_detail', args=[self.slug])


