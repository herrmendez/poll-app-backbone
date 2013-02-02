#from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource
from polls.models import Poll, Choice


class PollResource(ModelResource):
    choices = fields.ToManyField('polls.api.ChoiceResource', 'choice_set', full=True)

    class Meta:
        queryset = Poll.objects.all()
        resource_name = 'poll'


class ChoiceResource(ModelResource):
    poll = fields.ForeignKey(PollResource, 'poll')

    class Meta:
        queryset = Choice.objects.all()
        resource_name = 'choice'

