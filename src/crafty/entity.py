#! /usr/bin/env python
# -*- coding: UTF8 -*-
"""
############################################################
Entity Module
############################################################

:Author: *Carlo E. T. Oliveira*
:Contact: carlo@nce.ufrj.br
:Date: 2014/09/17
:Status: This is a "work in progress"
:Revision: 0.1.0
:Home: `Labase <http://labase.selfip.org/>`__
:Copyright: 2013, `GPL <http://is.gd/3Udt>`__.

.. moduleauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

"""
from .graphics import Sprite


class Entity(Sprite):
    """Creates an entity.  :ref:`entity`

    Any arguments will be applied in the same way .addComponent()
    is applied as a quick way to add components.

    Any component added will augment the functionality of the created entity by
    assigning the properties and methods from the component to the entity.

    :param: stage: Element to which entity will be attached to
    :param: cmp: Componente name
    :returns: An instance of Entity
    """
    def __init__(self, stage, cmp):
        self.__elt = stage.e(cmp)
        #super(self, Sprite, self.__elt)
        Sprite.__init__(self, self.__elt)
        self.__stage = stage

    def attr(self, **kwarg):
        """Set attributes.  :mod:`crafty.entity`

        :param: kwargs: keyword parameters with name and values of arguments to be changed
        :returns: Self, this same entity
        """
        #print(kwarg)
        self.__elt.attr(dict(**kwarg))
        return self

    def color(self, col):
        """Creates an entity.  :mod:`crafty.entity`

        :param: col: new color of the entity
        :returns: Self, this same entity
        """
        self.__elt.color(col)
        return self  # .__elt

    def fourway(self, way):
        """Creates an entity.  :mod:`crafty.entity`

        :param: way: the way of control
        :returns: Self, this same entity
        """
        self.__elt.requires('Fourway')
        self.__elt.fourway(way)
        return self  # .__elt

    def gravity(self, elt):
        """Creates gravity to entity.  :mod:`crafty.entity`

        :param: elt: entity to gravitate to
        :returns: Self, this same entity
        """
        self.__elt.requires('Gravity')
        self.__elt.gravity(elt)
        return self  # .__elt

    def _reel(self, reelId, duration, fromX, fromY, frameCount):
        """Create animation reel.

        :param: reelId: String name for this reel
        :param: duration: Duration time in miliseconds for this reel
        :param: fromX: reelId, Duration duration, Number fromX, Number fromY, Number frameCount
        :param: fromY: reelId, Duration duration, Number fromX, Number fromY, Number frameCount
        :param: frameCount: reelId, Duration duration, Number fromX, Number fromY, Number frameCount
        :returns: Self, this same entity
        """
        self.__elt.requires('SpriteAnimation')
        self.__elt.reel(reelId,  duration, fromX, fromY, frameCount)
        return self

    def _animate(self, reelId=None, loopCount=1):
        """Animate Entity.

        :param reelId: String reel identification
        :param loopCount:  Integer number of loops, default 1, indefinite if -1
        :returns: Self, this same entity
        """
        self.__elt.requires('SpriteAnimation')
        if reelId:
            self.__elt.animate(reelId,  loopCount)
        else:
            self.__elt.animate(loopCount)
        return self
