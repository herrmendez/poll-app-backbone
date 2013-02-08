#from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import DjangoAuthorization, Authorization
from polls.models import Poll, Choice
import pdb

class PollResource(ModelResource):
    #choices = fields.ToManyField('polls.api.ChoiceResource', 'choice_set', full=True)

    def __init__(self, api_name=None):
        super(PollResource, self).__init__(api_name=None)
        

    class Meta:
        queryset = Poll.objects.all()
        resource_name = 'poll'
        allowed_methods = ['get', 'post', 'put', 'delete']
        trailing_slash = False
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()


class ChoiceResource(ModelResource):
    poll = fields.ForeignKey(PollResource, 'poll')

    class Meta:
        queryset = Choice.objects.all()
        resource_name = 'choice'
        allowed_methods = ['get', 'post', 'put', 'delete']

from django.db import models
from django.contrib.auth.models import User
from tastypie.models import create_api_key

models.signals.post_save.connect(create_api_key, sender=User)
