from django.urls import reverse
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.views.generic import View
from django.utils.translation import ugettext_lazy as _
from .models import Link

class LinkRedirectView(View):
    def get(self, request, shortened_url):
        link
        try:
            link = Link.objects.get(shortened_url=shortened_url)
        except Link.DoesNotExist:
            return HttpResponseBadRequest("URL does not exist")
        return HttpResponseRedirect(link.full_url)
        
link_redirect_view = LinkRedirectView.as_view()
