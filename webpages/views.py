from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Sample
from django.template import loader

def index(request):
    all_samples = Sample.objects.all()
    template = loader.get_template('webpages/index.html')
    context = {
        'all_samples': all_samples,
    }
    return HttpResponse(template.render(context, request))

def detail(request, sample_id):
    return HttpResponse("<h2>Details for Sample id: " + str(sample_id) + "</h2>")