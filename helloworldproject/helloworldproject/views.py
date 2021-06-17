from django.http.response import HttpResponse
from django.http import HttpResponse

def helloworldfuction(request):
    returnedobject =  HttpResponse('<h1>hello world</h1>')
    return returnedobject