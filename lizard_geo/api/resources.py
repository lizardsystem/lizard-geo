from djangorestframework.resources import ModelResource

from lizard_geo.models import GeoObjectGroup


class GeoObjectGroupResource(ModelResource):
    """
    Resource for geo object group.

    TODO: what if no categories are associated? They are stored in the
    lizard-area mode....
    """
    model = GeoObjectGroup
    fields = ('name', 'slug', 'created_by', 'last_modified', 'categories', )
    ordering = ('name', )

    def categories(self, instance):
        return [
            {'name': category.name,
             'url': category.get_absolute_url()}
            for category in instance.category_set.all()]
