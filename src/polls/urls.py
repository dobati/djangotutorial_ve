from django.conf.urls import patterns, url
from polls import views

urlpatterns = patterns('',
    url(r'^$', 'polls.views.index', name='index'),
)