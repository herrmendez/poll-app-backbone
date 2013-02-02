from django.conf.urls import patterns, include, url
from tastypie.api import Api

from polls.api import PollResource, ChoiceResource

v1_api = Api(api_name='v1')
v1_api.register(PollResource())
v1_api.register(ChoiceResource())

urlpatterns = patterns('',
    url(r'api/', include(v1_api.urls)),
)
