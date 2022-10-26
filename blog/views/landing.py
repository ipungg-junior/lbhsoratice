from django.shortcuts import render
from django.views import View


class Landing(View):
    context = ''
    html = 'landing/index.html'

    def get(self, request):
        return render(request, template_name=self.html, context={}, content_type='text/html')    

    def post(self, request):
        pass