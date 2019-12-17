from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, Model
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class Link(Model):

    # De facto url max-length is 2000:
    # https://stackoverflow.com/questions/417142/what-is-the-maximum-length-of-a-url-in-different-browsers
    full_url = CharField(_("Full url"), max_length=2000)

    short_url = CharField(_("Shortened url"), max_length=10, unique=True)