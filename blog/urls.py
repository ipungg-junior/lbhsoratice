from django.urls import path
from blog.views.landing import Landing
from blog.views.blog import Blog

urlpatterns = [
    path('', Landing.as_view(context='landing')),
    path('blog/', Blog.as_view(context='blog-list')),
    path('blog/<slug:title>/', Blog.as_view(context='blog-detail')),
]
