from .models import Link
from rest_framework import serializers


class LinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Link
        fields = ['full_url', 'short_url']


