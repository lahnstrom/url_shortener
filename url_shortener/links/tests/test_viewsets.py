from django.test import TestCase
from rest_framework.test import APIRequestFactory
from ..viewsets import LinkViewSet
from ..models import Link


class ViewsetTest(TestCase):

    def fake_post_request_with(self, full_url='https://google.com', short_url='valid'):
        factory = APIRequestFactory()
        return factory.post('/links/', {'full_url': full_url, 'short_url': short_url})

    def test_post_link(self):

        short_url = 'unique'
        request = self.fake_post_request_with(short_url=short_url)
        link_create = LinkViewSet.as_view({'post': 'create'})
        link_create(request)
        try:
            Link.objects.get(short_url=short_url)
        except Link.DoesNotExist:
            self.fail()

    def test_post_bad_url_should_return_400(self):
        request = self.fake_post_request_with(short_url='/links//')
        link_create = LinkViewSet.as_view({'post': 'create'})
        response = link_create(request)

        self.assertEqual(response.status_code, 400)

    def test_post_too_short_url_should_return_400(self):
        request = self.fake_post_request_with(short_url='a')
        link_create = LinkViewSet.as_view({'post': 'create'})
        response = link_create(request)

        self.assertEqual(response.status_code, 400)
