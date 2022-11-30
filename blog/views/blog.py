from django.shortcuts import render
from django.views import View
from blog.models import Article

class Blog(View):
    context = ''
    blog_list_html = 'blog/blog-list.html'
    blog_detail_html = 'blog/blog-detail-mirror.html'

    def get(self, request, title=''):
        if (self.context=='blog-list'):
            article_list = Article.objects.all()
            # top_article = []
            # for i in article_list:
            #     topCount = 0
            #     if i.
            return render(request, template_name=self.blog_list_html, content_type='text/html', context={
                'article_list': article_list
            })    

        if (self.context=='blog-detail'):
            article = Article.objects.get(slug=title)
            article_tag = article.tag.all()

            # Mencari berita terkait (tag)
            suggestion = ''
            for i in article_tag:
                suggest = Article.objects.filter(tag=i)
                suggestion = suggest
            return render(request, template_name=self.blog_detail_html, context={'article': article, 'suggestion': suggestion}, content_type='text/html')   

    def post(self, request):
        pass
