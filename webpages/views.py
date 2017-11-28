from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .forms import UserForm
from .models import Sample
from django.http import HttpResponse
from django.template import loader
#
def index(request):

    all_samples = Sample.objects.all()
    template = loader.get_template('webpages/index.html')
    context = {
        'all_samples': all_samples,
    }
    return HttpResponse(template.render(context, request))

#
# def index(request):
#     samples = Sample.objects.all()
#     return render(request, 'webpages/index.html', {'samples': samples})



def detail(request, sample_id):

    #return HttpResponse("<h2>Details for Sample id: " + str(sample_id) + "</h2>")
    sample = get_object_or_404(Sample, pk=sample_id)
    return render(request, 'webpages/detail.html', {'sample': sample})

#
# def detail(request, album_id):
#     if not request.user.is_authenticated():
#         return render(request, 'music/login.html')
#     else:
#         user = request.user
#         album = get_object_or_404(Album, pk=album_id)
#         return render(request, 'music/detail.html', {'album': album, 'user': user})
