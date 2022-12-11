from django.shortcuts import render
from django.views import View
from blog.service.rendering import render_response

class Landing(View):
    context = ''
    html = 'landing/index.html'

    def get(self, request):
        return_object = render(request, template_name=self.html, context={}, content_type='text/html')    
        return render_response(return_object)

    def post(self, request):
        pass