from django.conf.urls import url
from .import views

app_name = 'webpages'

urlpatterns = [
    # /webpages/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # webpages/<sample_id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /webpages/sample/add/
    url(r'sample/add/$', views.SampleCreate.as_view(), name='sample-add'),

]
    # url(r'^$', views.index, name='index'),
    # #url(r'^webpages/', views.detail, name='detail'),
    #
    # #/webpages/ !
    # url(r'^webpages/', views.IndexView.as_view(), name='index'),
    #
    # url(r'^(?P<sample_id>[0-9]+)/$', views.detail, name='detail'),

