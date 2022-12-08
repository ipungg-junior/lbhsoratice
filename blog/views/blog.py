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
            top_article = []
            topCount = 0
            for i in article_list:
                if (i.visitor > topCount):
                    top_article = i
                    topCount = i.visitor
            return render(request, template_name=self.blog_list_html, content_type='text/html', context={
                'article_list': article_list,
                'top_article': top_article
            })    

        if (self.context=='blog-detail'):
            article = Article.objects.get(slug=title)
            article_tag = article.tag.all()

            # Mencari berita terkait (tag)
            suggestion = ''
            import random
            items = list(Article.objects.all())
            # change 3 to how many random items you want
            random_items = random.sample(items, 4)
            suggestion = random_items

            return render(request, template_name=self.blog_detail_html, context={'article': article, 'suggestion': suggestion}, content_type='text/html')   

    def post(self, request):
        pass
