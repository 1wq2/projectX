from django.conf.urls import url
from .import views


urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    #/webpages/
    url(r'^$', views.index, name='index'),

    # /music/id/
    url(r'^(?P<sample_id>[0-9]+)/$', views.detail, name='detail'),
]
