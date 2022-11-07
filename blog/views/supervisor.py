from django.shortcuts import render
from django.views import View

class Supervisor(View):

    context = ''

    def get(self, request):
        if (self.context=='dashboard'):
            return render(request, template_name='supervisor/dashboard.html', context={})
        pass

    def post(self, request):
        pass