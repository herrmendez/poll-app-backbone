from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from tastypie.api import Api
from polls.api import *

v1_api = Api(api_name='v1')
v1_api.register(PollResource())
v1_api.register(ChoiceResource())


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$', 'polls.views.index', name='index'),
    #url(r'^polls/', include('polls.urls')),
    url(r'api/', include(v1_api.urls)),
)


urlpatterns += staticfiles_urlpatterns()

