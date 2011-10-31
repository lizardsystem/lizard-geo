from djangorestframework.views import View

from lizard_geo.models import GeoObjectGroup


class RootView(View):
    """
    Startpoint.
    """
    def get(self, request):
        return {
            "geo_object_groups": [
                {'name': gog.name,
                 'url': gog.get_absolute_url()}
                for gog in GeoObjectGroup.objects.all()],
            }
