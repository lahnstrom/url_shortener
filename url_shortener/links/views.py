from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.views.generic import View
from django.shortcuts import get_object_or_404

from .models import Link


class LinkRedirectView(View):
    def get(self, request, short_url):
        link = get_object_or_404(Link, short_url=short_url)

        if link.has_expired:
            return HttpResponseBadRequest("URL Has Expired")

        link.increment_redirect_count()
        return HttpResponseRedirect(link.full_url)


link_redirect_view = LinkRedirectView.as_view()
