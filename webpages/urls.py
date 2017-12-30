from django.conf.urls import url
from .import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView



app_name = 'webpages'

urlpatterns = [


    # /webpages/
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    #url(r'^login_user/$', views.login_user, name='login_user'),
    #url(r'^logout_user/$', views.logout_user, name='logout_user'),

    url(r'^login_user/$', LoginView.as_view(template_name='webpages/login.html'), name='login_user'),
    #url(r'^logout_user/$', views.LogoutView.as_view(), name='logout_user'),
    url(r'^logout_user/$', LogoutView.as_view(template_name='webpages/login.html'), name='logout_user'),

    # webpages/<sample_id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /webpages/sample/add/
    url(r'sample/add/$', views.SampleAdd.as_view(), name='sample-add'),

    # /webpages/create/
    url(r'createSite/$', views.createSite.as_view(), name='createSite'),

    # /webpages/sample/2/
    url(r'sample/(?P<pk>[0-9]+)/$', views.SampleUpdate.as_view(), name='sample-update'),

    # /webpages/sample/2/delete/
    url(r'sample/(?P<pk>[0-9]+)/delete/$', views.SampleDelete.as_view(), name='sample-delete'),


]







    # url(r'^$', views.index, name='index'),
    # #url(r'^webpages/', views.detail, name='detail'),
    #
    # #/webpages/ !
    # url(r'^webpages/', views.IndexView.as_view(), name='index'),
    #
    # url(r'^(?P<sample_id>[0-9]+)/$', views.detail, name='detail'),

