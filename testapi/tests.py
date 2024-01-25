from django.test import TestCase
from django.urls import reverse

from testapi.models import Test
from testapi.api.v1.serializers import TestSerializers

class TestProject(TestCase):
    def setUp(self):
        self.test_project = Test.objects.creat(name='Test test project')

        def test_data(self):
            serializer = TestSerializers(self.test_project).data


class TestProjectView(TestCase):
    def setUp(self):
        self.test_project1 = Test.object.create(name='Test 1')
        self.test_project2 = Test.object.create(name='Test 2')

        self.url = reverse('test')