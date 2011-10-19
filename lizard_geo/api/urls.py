# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.
# from django.conf.urls.defaults import include
from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url
from django.contrib import admin

from djangorestframework.views import InstanceModelView

from lizard_geo.api.resources import GeoObjectGroupResource

from lizard_geo.api.views import RootView


admin.autodiscover()

NAME_PREFIX = 'lizard_geo_api_'

urlpatterns = patterns(
    '',
    url(r'^$',
        RootView.as_view(),
        name=NAME_PREFIX + 'root'),
    url(r'^geo_object_group/(?P<pk>[^/]+)/$',
        InstanceModelView.as_view(resource=GeoObjectGroupResource),
        name=NAME_PREFIX + 'geo_object_group'),
    )
