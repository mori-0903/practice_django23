from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def helloworldappview(request):
    return HttpResponse('app is called!!')
