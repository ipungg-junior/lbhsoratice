from django.urls import path
from blog.views.landing import Landing
from blog.views.blog import Blog
from blog.views.supervisor import Supervisor

urlpatterns = [
    path('', Landing.as_view(context='landing')),
    path('blog/', Blog.as_view(context='blog-list')),
    path('blog/<slug:title>/', Blog.as_view(context='blog-detail')),
    path('supervisor/', Supervisor.as_view(context='dashboard'))
]


from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)