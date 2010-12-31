from django import template
from django.core.cache import cache
from django.contrib.sites.models import Site

from simpleblocks.models import SimpleBlock
from simpleblocks.utils import get_cache_key, get_setting

register = template.Library()


def get_simple_block(parser, token):
    """
    Returns a block according to the key
    Blocks must be unique for site / language
    ``{% get_block KEY %}``
    Where ``KEY`` can be a variable or a string
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
        # figure out the key
        cache_key = get_cache_key(key, site)
        cached_content = cache.get(cache_key)
        if cached_content:
            return cached_content
        try:
            sblock = SimpleBlock.objects.get(site=site,
                                             key=key)
        except SimpleBlock.DoesNotExist:
            return ''
        cache.set(key, sblock.body, get_setting('TIMEOUT'))
        return sblock.body

register.tag('get_block', get_simple_block)
