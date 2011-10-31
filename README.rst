lizard-geo
==========================================

Introduction

Store geo objects and manage imports.

Development installation
------------------------

The first time, you'll have to run the bootstrap script to set up setuptools
and buildout::

    $> python bootstrap.py

And then run buildout to set everything up::

    $> bin/buildout

Note that on Microsoft Windows it is called ``bin\buildout.exe``.

You will have to re-run buildout when ``setup.py`` or ``buildout.cfg`` have
been modified, for example directly by you or through an update of your working
directory.

The current package is installed as a "development package", so changes in .py
files are automatically available (just like with ``python setup.py develop``).

The app lizard-area uses a SpatiaLite database, although this will probably be
overwritten at the site level. The repository already contains a SpatiaLite
database, so you should not need to create one yourself. In case you want to
create a new SpatiaLite database, execute the following command::

  $> spatialite lizard-area.db < init_spatialite-2.3.sql
  spatialite lizard-area.db < init_spatialite-2.3.sql
  SpatiaLite version ..: 2.3.0	Supported Extensions:
        - 'VirtualShape'        [direct Shapefile access]
        - 'VirtualText          [direct CSV/TXT access]
        - 'VirtualNetwork       [Dijkstra shortest path]
        - 'RTree'               [Spatial Index - R*Tree]
        - 'MbrCache'            [Spatial Index - MBR cache]
        - 'VirtualFDO'          [FDO-OGR interoperability]
        - 'SpatiaLite'          [Spatial SQL - OGC]
  PROJ.4 version ......: Rel. 4.7.1, 23 September 2009
  GEOS version ........: 3.1.0-CAPI-1.5.0

The above snippet assumes you already have installed SpatiaLite.

To create the database tables and fill them do::

  $ bin/django syncdb

.. _South: http://south.aeracode.org/

Several lizard packages use South_ to handle the creation of tables. The above
command will inform you which packages have to be handled by South. For
example, its output will contains messages such as these::

  Not synced (use migrations):
   - lizard_geo
   - lizard_ui
  (use ./manage.py migrate to migrate these)

You can create the tables for these packages, or using the South terminology,
'migrate' them, as follows::

  $ bin/django migrate

Usage
-----

Use lizard-area and lizard-fewsnorm as examples.

