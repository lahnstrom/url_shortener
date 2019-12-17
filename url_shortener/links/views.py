from django.urls import reverse
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.views.generic import View

from rest_framework import viewsets

from .models import Link
from .serializers import LinkSerializer

class LinkRedirectView(View):
    def get(self, request, shortened_url):
        link = None
        try:
            link = Link.objects.get(shortened_url=shortened_url)
        except Link.DoesNotExist:
            return HttpResponseBadRequest("URL does not exist")
        return HttpResponseRedirect(link.full_url)



class LinkViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows links to be viewed or edited.
    """
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


link_redirect_view = LinkRedirectView.as_view()
