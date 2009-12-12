from django.db import models
from django.conf import settings
from django.contrib.sites.models import Site

class SimpleBlock(models.Model):
    key = models.SlugField()
    body = models.TextField()
    site = models.ForeignKey(Site)
    
    def __unicode__(self):
        return u'%s: %s' % (self.key, self.body)
    
    class Meta:
        unique_together = (('key', 'site'),)
