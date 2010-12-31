from django.conf import settings
from simpleblocks import defaults

def get_setting(setting_key):
    prefix = 'SIMPLEBLOCKS_'
    if hasattr(settings, '%s%s' % (prefix, setting_key)):
        return getattr(settings, '%s%s' % (prefix, setting_key))
    else:
        return getattr(defaults, '%s%s' % (prefix, setting_key))


def get_cache_key(key, site):
    return '%s%s%s' % (get_setting('PREFIX'),
                       site.domain,
                       key)
