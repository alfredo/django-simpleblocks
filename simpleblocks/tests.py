from django.contrib.sites.models import Site
from django.test import TestCase
from django.template import Context, Template
from simpleblocks.models import SimpleBlock


def render_to_string(template, data):
    t = Template(template)
    c = Context(data)
    return t.render(c)

class SimpleBlocksTest(TestCase):
    
    def setUp(self):
        """
        Set ups the models
        """
        self.body = "Test body"
        self.site = Site.objects.get_current()
        self.block = SimpleBlock.objects.create(key='test',
                                                body=self.body,
                                                site=self.site)
        self.template = '{% load simpleblocks_tags %}{% get_block "test" %}'
        self.data = {}

    def tearDown(self):
        SimpleBlock.objects.all().delete()
    
    def testRenderedStatic(self):
        """
        Test the tag with a static key
        """
        rendered = render_to_string(self.template, self.data)
        self.assertEquals(rendered, self.body)

    def testRenderedVariable(self):
        """
        Test the tag with a variable key
        """
        data = {'test_variable': 'test'}
        template = '{% load simpleblocks_tags %}{% get_block test_variable %}'
        rendered = render_to_string(template, data)
        self.assertEquals(rendered, self.body)
