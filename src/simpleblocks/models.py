from django.db import models
from django.core.cache import cache
from simpleblocks.utils import get_cache_key, get_setting

class SimpleBlock(models.Model):
    key = models.SlugField()
    body = models.TextField()
    site = models.ForeignKey('sites.Site')

    class Meta:
        unique_together = (('key', 'site'),)

    def __unicode__(self):
        return u'Key %s: %s' % (self.key, self.body)

    def save(self, *args, **kwargs):
        # update cache on save
        cache_key = get_cache_key(self.key, self.site)
        cache.set(cache_key, self.body, get_setting('TIMEOUT'))
        super(SimpleBlock, self).save(*args, **kwargs)
