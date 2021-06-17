from django.http.response import HttpResponse
from django.http import HttpResponse
from django.views.generic import TemplateView

def helloworldfuction(request):
    returnedobject =  HttpResponse('<h1>hello world</h1>')
    return returnedobject

class Helloworldclass(TemplateView):
    template_name = 'hello.html'

