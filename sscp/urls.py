from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from sscp.views import *

urlpatterns = patterns('',
                       #url(r'list', views.list, name='list'),
                       #url(r'manual', views.manualIndex, name='manualIndex'),
                       #url(r'term', views.terminal, name='terminal'),
                       #url(r'detail/(\d+)', views.detail, name='detail'),
                       url(r'list', FilmList.as_view()),
                       url(r'test', TemplateView.as_view(template_name='sscp\\test.html')),
                       )