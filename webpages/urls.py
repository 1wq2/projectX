from django.conf.urls import url
from .import views

app_name = 'webpages'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^webpages/', views.detail, name='detail'),

    url(r'^(?P<sample_id>[0-9]+)/$', views.detail, name='detail'),
]
