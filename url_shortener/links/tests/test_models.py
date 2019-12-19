from datetime import timedelta
from django.test import TestCase
from django.core.exceptions import ValidationError
from django.utils import timezone
from url_shortener.links.models import Link


class LinkTest(TestCase):

    def create_link(self, expires_at=None, short_url="asdf", full_url="https://google.com"):
        return Link.objects.create(short_url=short_url, full_url=full_url, expires_at=expires_at)

    def test_creation_of_link(self):
      link = self.create_link()
      assert isinstance(link, Link)

    def test_has_expired(self):
      yesterday = timezone.now() - timedelta(days=1)
      link = self.create_link(expires_at=yesterday)
      assert link.has_expired

      tomorrow = timezone.now() + timedelta(days=1)
      link_2 = self.create_link(expires_at=tomorrow, short_url="banan")
      assert not link_2.has_expired
