from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$', 'polls.views.index', name='index'),
    url(r'^polls/', include('polls.urls')),
)


urlpatterns += staticfiles_urlpatterns()

