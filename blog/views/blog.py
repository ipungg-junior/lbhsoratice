from django.shortcuts import render
from django.views import View


class Blog(View):
    context = ''
    blog_list_html = 'blog/blog-list.html'
    blog_detail_html = 'blog/blog-detail.html'

    def get(self, request):
        if (self.context=='blog-list'):
            return render(request, template_name=self.blog_list_html, context={}, content_type='text/html')    
        if (self.context=='blog-detail'):
            return render(request, template_name=self.blog_detail_html, context={}, content_type='text/html')   

    def post(self, request):
        pass