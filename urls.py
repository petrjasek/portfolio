from django.conf.urls.defaults import patterns, url
from views import *

urlpatterns = patterns('',
    url(r'^(?P<url>[-_a-z0-9]+)$', ProjectView.as_view(), name='project'),
    url(r'^$', IndexView.as_view(), name='index'),
)
