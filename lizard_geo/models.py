# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.
from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class GeoObjectGroup(models.Model):
    """
    Geo objects are grouped.

    These are starting points to navigate through all geo objects.

    Examples of groups:
    - Alle aan-/afvoergebieden van een waterschap
    - Alle deel aan-/afvoergebieden van 1 deelgebied
    - Alle krw waterlichamen

    TODO: Automatically fill in slug
    """
    name = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)
    # legend = models.ForeignKey(LegendClass, null=True, blank=True)
    # "source"

    created_by = models.ForeignKey(User)
    last_modified = models.DateTimeField(auto_now=True)
    source_log = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('lizard_geo_api_geo_object_group',
                       kwargs={'pk': self.pk})


class GeoObject(models.Model):
    """
    Geo objects storage.

    Ident MUST be unique. When importing shapefiles references are
    done using ident.

    Parents are used for deel aan-/afvoergebieden.
    """
    ident = models.CharField(max_length=80, unique=True)
    geometry = models.GeometryField(srid=4326)
    geo_object_group = models.ForeignKey(GeoObjectGroup)
    objects = models.GeoManager()

    # verwijzing naar "bron locatie" string

    def __unicode__(self):
        return '%s (%s)' % (self.ident, self.geo_object_group)


