from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1> Webpages page is currently in the development. Please be patient</h1>")