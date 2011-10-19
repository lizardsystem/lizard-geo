# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.
from django.conf.urls.defaults import include
from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url
from django.contrib import admin

from lizard_ui.urls import debugmode_urlpatterns

admin.autodiscover()


API_URL_NAME = 'lizard_geo_api_root'

urlpatterns = patterns(
    '',
    (r'^api/', include('lizard_geo.api.urls')),
    )
urlpatterns += debugmode_urlpatterns()
