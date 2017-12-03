from django.conf.urls import url
from .import views



urlpatterns = [

    # HOME PAGE!!!
    url(r'^$', views.VisitorView.as_view(), name='index'),

]