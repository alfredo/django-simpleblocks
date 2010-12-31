from django.db import models

class SimpleBlock(models.Model):
    key = models.SlugField()
    body = models.TextField()
    site = models.ForeignKey('sites.Site')

    def __unicode__(self):
        return u'Key %s: %s' % (self.key, self.body)

    class Meta:
        unique_together = (('key', 'site'),)
