from django.shortcuts import render
from django.views import View
from blog.models import Article

class Blog(View):
    context = ''
    blog_list_html = 'blog/blog-list.html'
    blog_detail_html = 'blog/blog-detail.html'

    def get(self, request):
        if (self.context=='blog-list'):
            blog_list = Article.objects.all()[:40]
            print(blog_list[0].content)
            return render(request, template_name=self.blog_list_html, content_type='text/html', context={
                'article': blog_list
            })    
        if (self.context=='blog-detail'):
            return render(request, template_name=self.blog_detail_html, context={}, content_type='text/html')   

    def post(self, request):
        pass