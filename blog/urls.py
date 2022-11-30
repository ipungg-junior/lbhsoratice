from django.urls import path
from blog.views.landing import Landing
from blog.views.blog import Blog
from blog.views.supervisor import Supervisor
from blog.views.microservice import Microservice    # handle semua API Backend

urlpatterns = [
    path('', Landing.as_view(context='landing')),
    path('blog/', Blog.as_view(context='blog-list')),
    path('blog/<slug:title>/', Blog.as_view(context='blog-detail')),
    path('supervisor/', Supervisor.as_view(context='dashboard')),
    path('supervisor/edit/<slug:title>/', Supervisor.as_view(context='edit-article')),
    path('supervisor/upload-article/', Supervisor.as_view(context='upload-article')),
    path('supervisor/accounts/', Supervisor.as_view(context='accounts')),
    path('supervisor/accounts/register/', Supervisor.as_view(context='register-account')),
    path('supervisor/accounts/<int:accountId>', Supervisor.as_view(context='account-detail')),
    # API
    path('blog-service/report-visitor/', Microservice.as_view(context='report-visitor')),
]


