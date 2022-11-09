import json
from django.views import View
from django.http import HttpResponse
from blog.models import Article


class Microservice(View):

    context = ''

    def post(self, request):
        if (self.context == 'report-visitor'):
            data_str = (request.body).decode('utf-8')
            request_bodyjson = json.loads(data_str)
            article = Article.objects.get(slug=request_bodyjson['slug'])
            article.visitor += 1
            article.save()
            return HttpResponse(status=200)