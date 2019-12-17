from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.views.generic import View

from .models import Link

class LinkRedirectView(View):
    def get(self, request, short_url):
        link = None
        
        try:
            link = Link.objects.get(short_url=short_url)
        except Link.DoesNotExist:
            return HttpResponseBadRequest("URL does not exist")

        if link.has_expired():
            return HttpResponseBadRequest("URL Has Expired")

        link.increment_redirect_count()
        return HttpResponseRedirect(link.full_url)


link_redirect_view = LinkRedirectView.as_view()
