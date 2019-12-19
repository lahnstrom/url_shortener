from django.urls import path, include
from rest_framework import routers

from .views import link_redirect_view
from .viewsets import LinkViewSet

router = routers.DefaultRouter()
router.register(r'links', LinkViewSet, basename='links')

app_name = "links"
urlpatterns = [
    path('', include(router.urls)),
    path("<str:short_url>", view=link_redirect_view, name="redirect"),
]
