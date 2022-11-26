from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from blog.models import Article, Tag, UserAccount
import json, base64
from django.core.files.base import ContentFile
from blog.form import ArticleContentForm
from blog.service.account import Account

class Supervisor(View):

    context = ''

    def get(self, request, title=''):
        if (self.context=='dashboard'):
            article_query = Article.objects.all()
            return render(request, template_name='supervisor/dashboard.html', context={
                'article_query': article_query
            })
        if (self.context=='upload-article'):
            contentForm = ArticleContentForm()
            resp = render(request, template_name='supervisor/upload.html', context={'contentForm': contentForm})
            resp['cache-control'] = "no-cache"
            return resp

        if (self.context=='edit-article'):
            article_query = Article.objects.get(slug=title)
            contentForm = ArticleContentForm()
            resp = render(request, template_name='supervisor/edit.html', context={'article': article_query, 'contentForm': contentForm})
            resp['cache-control'] = "no-cache"
            return resp
        if (self.context=='accounts'):
            account_query = UserAccount.objects.all()
            resp = render(request, template_name='supervisor/account.html', context={'account_query':account_query})
            resp['cache-control'] = "no-cache"
            return resp



    def post(self, request, title=''):
        if (self.context == 'upload-article'):
            data_str = (request.body).decode('utf-8')
            request_bodyjson = json.loads(data_str)
            tag = Tag.objects.all()[0]
            title = request_bodyjson['title']
            slug = (title.lower()).replace(' ', '-')
            content = request_bodyjson['content']
            base64image = request_bodyjson['img']
            format, imgstr = base64image.split(';base64,') 
            ext = format.split('/')[-1] 
            data = ContentFile(base64.b64decode(imgstr), name=f'{title}.{ext}')
            print(base64image)
            # new_article = Article.objects.create(
            #     title=title,
            #     img=data,
            #     slug=slug,
            #     content=content,
            #     visitor=0
            #     )
            # new_article.save()
            try:
                return HttpResponse(status=200)
            except:
                return HttpResponse(status=500)

        if (self.context == 'edit-article'):
            article = Article.objects.get(slug=title)
            data_str = (request.body).decode('utf-8')
            request_bodyjson = json.loads(data_str)
            tag = Tag.objects.all()[0]
            title = request_bodyjson['title']
            slug = (title.lower()).replace(' ', '-')
            content = request_bodyjson['content']
            base64image = request_bodyjson['img']
            format, imgstr = base64image.split(';base64,') 
            ext = format.split('/')[-1] 
            data = ContentFile(base64.b64decode(imgstr), name=f'{title}.{ext}')
            article.title = title
            article.slug = slug
            article.content = content
            article.img = data
            article.save()
            return HttpResponse(status=200)


        if (self.context == "register-account"):
            request_body = (request.body).decode('utf-8')
            request_body = json.loads(request_body)
            try:
                new_account = Account.create_new_account(request_body)
                return HttpResponse(status=200)
            except:
                return HttpResponse(status=500)