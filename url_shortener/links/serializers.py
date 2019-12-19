from rest_framework import serializers
from .models import Link


class LinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Link
        fields = ['full_url', 'short_url', 'redirect_count', 'uuid', 'expires_at']
