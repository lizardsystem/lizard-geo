# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.

from django.test import TestCase

from lizard_geo.api.resources import GeoObjectGroupResource


class ApiTest(TestCase):

    def test_smoke_resource(self):
        GeoObjectGroupResource(None)
