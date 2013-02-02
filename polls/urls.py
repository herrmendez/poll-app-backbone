from django.conf.urls import patterns, include, url
from polls.api import PollResource, ChoiceResource

poll_resource = PollResource()
choice_resource = ChoiceResource()

urlpatterns = patterns('',
    url(r'api/', include(poll_resource.urls)),
    url(r'api/', include(choice_resource.urls)),

)
