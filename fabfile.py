# -*- coding: utf-8 -*-
"""
############################################################
Brython Crafty -  - Fabric deployment
############################################################

:Author: *Carlo E. T. Oliveira*
:Contact: carlo@nce.ufrj.br
:Date: $Date: 2014/10/10  $
:Status: This is a "work in progress"
:Revision: $Revision: 0.01 $
:Home: `Labase <http://labase.nce.ufrj.br/>`__
:Copyright: ©2013, `GPL <http://is.gd/3Udt>__.
"""
from fabric.api import local  # , settings, cd, run, lcd
#from tempfile import mkdtemp
KG_ORIGIN = '/home/carlo/Documentos/dev/brython_crafty/src/crafty/'
KG_DEST = '/home/carlo/Documentos/dev/lib/Brython2.2/Lib/site-packages/crafty'
PN_DEST = '/home/carlo/Documentos/dev/brython-in-the-classroom/pyschool/static/external/brython/Lib/site-packages/crafty'
SOURCES = '*.py'
FILENAMES = 'base.py entity.py extra.py	__init__.py utils.py core.py graphics.py jscrafty.py'.split()


def _do_copy(source, targ):
    #local("mkdir -p %s" % targ)
    local("cp -u %s -t %s" % (source, targ))


def _k_copy(targ):
    for part in FILENAMES:
        _do_copy(KG_ORIGIN+part, targ)


def deploy():
    _k_copy(KG_DEST)
    _k_copy(PN_DEST)
    #kzip()
