from django import template
from django.core.cache import cache
from django.conf import settings
from django.contrib.sites.models import Site

from simpleblocks import defaults
from simpleblocks.models import SimpleBlock

register = template.Library()        

def get_setting(setting_key):
    prefix = 'SIMPLEBLOCKS_'
    if hasattr(settings, '%s%s' % (prefix, setting_key)):
        return getattr(settings, '%s%s' % (prefix, setting_key))
    else:
        return getattr(defaults, '%s%s' % (prefix, setting_key))

def get_simple_block(parser, token):
    """
    Returns a block according to the key
    Blocks must be unique for site / language
    USAGE:
    
    {% get_block KEY %}

    KEY can be a variable or a string
    """
    bits = token.contents.split()
    if len(bits) != 2:
        raise template.TemplateSyntaxError("'%s' tag takes exaclty one argument" % bits[0])
    key = parser.compile_filter(bits[1])
    return SimpleBlockNode(key)

class SimpleBlockNode(template.Node):

    def __init__(self, key):
        self.key = key

    def render(self, context):
        key = self.key.resolve(context, True)
        site = Site.objects.get_current()
        cache_key = '%s%s%s' % (get_setting('PREFIX'),
                                site.domain,
                                key)
        cached_key = cache.get(cache_key)
        if cached_key:
            return cached_key
        else:
            try:
                sblock = SimpleBlock.objects.get(site=site,
                                                 key=key)                
            except SimpleBlock.DoesNotExist:
                return ''
            cache.set(key, sblock.body, get_setting('TIMEOUT'))
            return sblock.body
        return ''

register.tag('get_block', get_simple_block)
