# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.
from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class GeoObjectGroup(models.Model):
    """Implements a group of GeoObject(s).

    A GeoObjectGroup can be a starting point to navigate through a specific
    subset of GeoObject(s).

    TODO: Automatically fill in slug
    """
    name = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)

    created_by = models.ForeignKey(User)
    last_modified = models.DateTimeField(auto_now=True)
    source_log = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('lizard_geo_api_geo_object_group',
                       kwargs={'pk': self.pk})


class GeoObject(models.Model):
    """Represents a real-world geometrical entity or is linked to one.

    A GeoObject 'as is' only contains basic information. In general, you will
    have to extend this information in a subclass.

    Note that field 'ident' should be unique. This field will contain
    an ID for the GeoObject in the terminology of the domain
    field. Client code can use this field to query and/or filter. If
    multiple items are returned, the user must contact the
    administrator to remove one of the rows from the source data.

    """
    ident = models.CharField(max_length=80)
    geometry = models.GeometryField(srid=4326)
    geo_object_group = models.ForeignKey(GeoObjectGroup)
    objects = models.GeoManager()

    # verwijzing naar "bron locatie" string

    def __unicode__(self):
        return '%s (%s)' % (self.ident, self.geo_object_group)

    def extent(self, srid=900913):
        """ return a tuple with extent

        note: tuple is needed in templates (including braces) in
        template homepage.js
        """

        return self.geometry.transform(srid, True).extent
