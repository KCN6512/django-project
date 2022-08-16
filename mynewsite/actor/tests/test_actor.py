import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mynewsite.settings")
import django
django.setup()

from django.test import TestCase
from actor.models import *

class ActorTestCase(TestCase):
    def setUp(self):
        Actor.objects.create(title="test1", cat_id=3)
        Actor.objects.create(title="test2")

    def test_test(self):
        first = Actor.objects.get(title="test1")
        second = Actor.objects.get(title="test2")
        self.assertEqual(first.title, 'test1')
        self.assertEqual(first.cat.name, 'Смешарики')
        self.assertEqual(second.title, 'test2')