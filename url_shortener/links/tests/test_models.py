from django.test import TestCase
from url_shortener.links.models import Link


class LinkTest(TestCase):

    def create_link(self, expires_at, short_url="asdf", full_url="https://google.com"):
        return Link.objects.create(short_url=short_url, full_url=full_url, expires_at=expires_at)
