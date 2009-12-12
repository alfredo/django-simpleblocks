from django.contrib import admin
from simpleblocks.models import SimpleBlock

class SimpleBlockAdmin(admin.ModelAdmin):
    list_display = ('key', 'site', 'body')
    search_fields = ['key', 'body']
    list_filter = ('site',)

admin.site.register(SimpleBlock, SimpleBlockAdmin)
