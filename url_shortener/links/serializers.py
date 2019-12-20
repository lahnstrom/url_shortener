from rest_framework import serializers
from .utils import short_url_regex, url_regex
from .models import Link


class LinkSerializer(serializers.HyperlinkedModelSerializer):
    short_url = serializers.RegexField(short_url_regex,)
    full_url = serializers.RegexField(url_regex)

    class Meta:
        model = Link
        fields = ['full_url', 'short_url', 'redirect_count', 'uuid', 'expires_at', 'created_at', 'updated_at']
