from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import Sample
from django.http import HttpResponse
from django.template import loader

from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy
from .models import Sample
from .forms import UserForm
from django.contrib.auth.mixins import LoginRequiredMixin

#############################

from django.utils.http import is_safe_url
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import FormView, RedirectView

from django.contrib.auth import login
class VisitorView(generic.TemplateView):
    template_name = 'webpages/base_visitor.html'

class IndexView(LoginRequiredMixin, generic.ListView):
    login_url = '/webpages/login_user'
    redirect_field_name = 'redirect_to'

    template_name = 'webpages/index.html'
    context_object_name = 'samples' #all_samples

    def get_queryset(self):
        print(self.request.user)
        return Sample.objects.filter(user=self.request.user)


class DetailView(LoginRequiredMixin, generic.DeleteView):
    login_url = '/webpages/login_user'
    redirect_field_name = 'redirect_to'

    model = Sample
    template_name = 'webpages/detail.html'




class SampleCreate(LoginRequiredMixin, CreateView):
    login_url = '/webpages/login_user'
    redirect_field_name = 'redirect_to'

    model = Sample
    fields = ['sample_logo', 'sample_title']

    def form_valid(self, form):
        object = form.save(commit=False)
        object.user = self.request.user
        object.save()
        return super(SampleCreate, self).form_valid(form)

class SampleUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/login_user/'
    redirect_field_name = 'redirect_to'

    model = Sample
    fields = ['sample_logo', 'sample_title']

    def form_valid(self, form):
        object = form.save(commit=False)
        object.user = self.request.user
        object.save()
        return super(SampleUpdate, self).form_valid(form)

class SampleDelete(LoginRequiredMixin, DeleteView):
    login_url = '/login_user/'
    redirect_field_name = 'redirect_to'

    model = Sample
    success_url = reverse_lazy('webpages:index')

class UserFormView(View):
    form_class = UserForm
    template_name = 'webpages/registration_form.html'

    #display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form })

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            # cleaned(normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User objects if correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('webpages:index')
        return render(request, self.template_name, {'form': form})
#
        #
        #
        # def logout_user(request):
        #     logout(request)
        #     form = UserForm(request.POST or None)
        #     context = {
        #         "form": form,
        #     }
        #     return render(request, 'webpages/login.html', context)
        #
        #
        # def login_user(request):
        #     if request.method == "POST":
        #         username = request.POST['username']
        #         password = request.POST['password']
        #         user = authenticate(username=username, password=password)
        #         if user is not None:
        #             if user.is_active:
        #                 login(request, user)
        #                 albums = Album.objects.filter(user=request.user)
        #                 return render(request, 'music/index.html', {'albums': albums})
        #             else:
        #                 return render(request, 'music/login.html', {'error_message': 'Your account has been disabled'})
        #         else:
        #             return render(request, 'music/login.html', {'error_message': 'Invalid login'})
        #     return render(request, 'music/login.html')





# #
# def index(request):
#
#     all_samples = Sample.objects.all()
#     template = loader.get_template('webpages/index.html')
#     context = {
#         'all_samples': all_samples,
#     }
#     return HttpResponse(template.render(context, request))
#
# #
# # def index(request):
# #     samples = Sample.objects.all()
# #     return render(request, 'webpages/index.html', {'samples': samples})
#
# class
#
#
# def detail(request, sample_id):
#
#     #return HttpResponse("<h2>Details for Sample id: " + str(sample_id) + "</h2>")
#     sample = get_object_or_404(Sample, pk=sample_id)
#     return render(request, 'webpages/detail.html', {'sample': sample})
#
#
# #
# # def detail(request, album_id):
# #     if not request.user.is_authenticated():
# #         return render(request, 'music/login.html')
# #     else:
# #         user = request.user
# #         album = get_object_or_404(Album, pk=album_id)
# #         return render(request, 'music/detail.html', {'album': album, 'user': user})
