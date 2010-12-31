from django.contrib.sites.models import Site
from django.db.utils import IntegrityError
from django.test import TestCase
from django.template import Context, Template

from simpleblocks.models import SimpleBlock


def render_to_string(template, data):
    t = Template(template)
    c = Context(data)
    return t.render(c)

class SimpleBlocksTest(TestCase):

    def setUp(self):
        """Actions to be executed before each test"""
        self.body = 'Test Body'
        self.site = Site.objects.get_current()
        self.template = '{% load simpleblocks_tags %}{% get_block "test" %}'
        self.data = {}

    def tearDown(self):
        """Actions to be executed after each test"""
        SimpleBlock.objects.all().delete()

    def create_block(self, key='test'):
        """Helper to create block"""
        data = {'body': self.body,
                'key': key,
                'site': self.site}
        return SimpleBlock.objects.create(**data)

    def testCreateBlock(self):
        """Test block creation"""
        data = {'body': self.body,
                'key': 'test',
                'site': self.site}
        block = SimpleBlock.objects.create(**data)
        assert block, 'Failed to create block'

    def testRenderedStatic(self):
        """Test the tag with a static key"""
        self.create_block()
        rendered = render_to_string(self.template, self.data)
        self.assertEquals(rendered, self.body)

    def testRenderedVariable(self):
        """Test the tag with a variable key"""
        self.create_block()
        data = {'test_variable': 'test'}
        template = '{% load simpleblocks_tags %}{% get_block test_variable %}'
        rendered = render_to_string(template, data)
        self.assertEquals(rendered, self.body)

    def testFailedDuplicated(self):
        """Test failure upon duplicated key and site"""
        self.create_block()
        with self.assertRaises(IntegrityError):
            self.create_block()
