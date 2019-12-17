from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class LinksConfig(AppConfig):
    name = "url_shortener.links"
    verbose_name = _("Links")

    def ready(self):
        try:
            import url_shortener.links.signals  # noqa F401
        except ImportError:
            pass
