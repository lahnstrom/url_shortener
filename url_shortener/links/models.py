import random
import string
import uuid

from django.core.validators import RegexValidator
from django.utils import timezone
from django.db.models import CharField, Model, IntegerField, UUIDField, DateTimeField
from django.utils.translation import ugettext_lazy as _

from .utils import url_regex, short_url_regex

url_default_length = 8


def generate_short_url():
    random_string = ''.join(random.choices(
        string.ascii_uppercase +
        string.ascii_lowercase +
        string.digits,
        k=url_default_length))

    return random_string


class Link(Model):

    # De facto url max-length is 2000:
    # https://stackoverflow.com/questions/417142/what-is-the-maximum-length-of-a-url-in-different-browsers
    full_url = CharField(_("Full url"), max_length=2000, validators=[RegexValidator(
        regex=url_regex,
        message='Enter a valid url starting with http')])

    short_url = CharField(_("Shortened url"),
                          max_length=url_default_length,
                          unique=True,
                          default=generate_short_url,
                          validators=[RegexValidator(regex=short_url_regex,
                                                     message=(_("Enter 4-8 alphanumeric characters")))])

    # Should increment on every redirect
    redirect_count = IntegerField(_("Redirect Count"), editable=False, default=0)

    uuid = UUIDField(default=uuid.uuid4, editable=False, unique=True)

    expires_at = DateTimeField(_('Expires At'), blank=True, null=True)

    @property
    def has_expired(self):
        if self.expires_at is None:
            return False
        return self.expires_at < timezone.now()

    def increment_redirect_count(self):
        self.redirect_count += 1
        self.save()

    def get_absolute_url(self):
        return f"links/{str(self.uuid)}"

    def __str__(self):
        return f"{self.short_url} -> {self.full_url}"
