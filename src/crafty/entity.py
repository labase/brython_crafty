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
from .base import Base


class Entity(Sprite, Base):
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
        self.__stage = stage
        #super(self, Sprite, self.__elt)
        Sprite.__init__(self, self.__elt)
        Base.__init__(self, self.__elt)

    def attach(self, entity):
        """Attach an entity to this one.  :mod:`crafty.entity`

        :param: entity: The entity to be attached
        :returns: Self, this same entity
        """
        self.__elt.attach(entity.entity)
        return self

    def color(self, col):
        """Creates an entity.  :mod:`crafty.entity`

        :param: col: new color of the entity
        :returns: Self, this same entity
        """
        self.__elt.color(col)
        return self

    def fourway(self, speed):
        """Creates an four way entity control.  :mod:`crafty.entity`

        :param: speed: the speed of movement
        :returns: Self, this same entity
        """
        self.__elt.requires('Fourway')
        self.__elt.fourway(speed)
        return self

    def multiway(self, speed, **directions):
        """Creates an four way entity control.  :mod:`crafty.entity`

        :param: speed: the speed of movement
        :param: directions: named directions and degree (UP_ARROW: -90, DOWN_ARROW: 90, RIGHT_ARROW: 0, LEFT_ARROW: 180)
        :returns: Self, this same entity
        """
        self.__elt.requires('Multiway')
        self.__elt.multiway(speed, dict(**directions))
        return self

    def gravity(self, elt):
        """Creates gravity to entity.  :mod:`crafty.entity`

        :param: elt: entity to gravitate to
        :returns: Self, this same entity
        """
        self.__elt.requires('Gravity')
        self.__elt.gravity(elt)
        return self

    @property
    def rotation(self):
        """Rotate entity.  :mod:`crafty.entity`

        :returns: Ammount of rotation
        """
        self.__elt.requires('2D')
        return self.__elt.rotation

    @rotation.setter
    def rotation(self, value):
        """Rotate entity.  :mod:`crafty.entity`

        :param: value: Ammount of rotation
        """
        self.__elt.requires('2D')
        self.__elt.rotation = value

    def origin(self, value):
        """Set rotation origin for entity.  :mod:`crafty.entity`

        :param: value: lef, top, right, bottom, center, middle
        :returns: Self, this same entity
        """
        self.__elt.requires('2D')
        self.__elt.origin(value)
        return self

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

    @property
    def visible(self):
        return None

    @visible.setter
    def visible(self, set_visibility):
        """Change Entity Visibility.

        :param set_visibility: String reel identification
        """
        self.__elt.visible = set_visibility

    @property
    def entity(self):
        """Entity property.

        """
        return self.__elt

    @entity.setter
    def entity(self, _):
        """Entity property is read only.

        :param _: Ignored
        """
        pass
