from rest_framework import viewsets, mixins

from .models import Link
from .serializers import LinkSerializer

class LinkViewSet(mixins.CreateModelMixin, 
                  mixins.RetrieveModelMixin, 
                  mixins.ListModelMixin, 
                  mixins.DestroyModelMixin, 
                  viewsets.GenericViewSet):
    """
    API endpoint that allows links to be listed, created and deleted.
    """
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    lookup_field = 'uuid'
