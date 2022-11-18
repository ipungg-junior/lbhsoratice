from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from blog.user_manager import UserManager

class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    

    # Client Manager Reuirements
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    objects = UserManager()

    def __str__(self):
        return self.email


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


