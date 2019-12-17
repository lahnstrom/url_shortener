import random
import string

from django.db.models import CharField, Model
from django.utils.translation import ugettext_lazy as _

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
    full_url = CharField(_("Full url"), max_length=2000)

    short_url = CharField(_("Shortened url"), max_length=url_default_length, unique=True, default=generate_short_url)

