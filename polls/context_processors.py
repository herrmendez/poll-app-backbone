import logging
from tastypie.models import ApiKey

logger = logging.getLogger(__name__)

def api_key(request):
    '''Return the api_key that belongs to the current user'''
    user = request.user
    try:
        api_key = ApiKey.objects.get(user=user)
    except:
        logger.error("anonymous users don't have an api_key")
    return api_key.key
