from django.urls import path

from url_shortener.links.views import (
    link_redirect_view,
)

app_name = "links"
urlpatterns = [
   path("<str:shortened_url>/", view=link_redirect_view, name="redirect"),
    # path("links/", view=link_view, name="link"),
]
