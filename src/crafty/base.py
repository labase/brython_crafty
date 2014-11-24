#! /usr/bin/env python
# -*- coding: UTF8 -*-
"""
############################################################
Base Module
############################################################

:Author: *Carlo E. T. Oliveira*
:Contact: carlo@nce.ufrj.br
:Date: 2014/09/23
:Status: This is a "work in progress"
:Revision: 0.1.0
:Home: `Labase <http://labase.selfip.org/>`__
:Copyright: 2013, `GPL <http://is.gd/3Udt>`__.

.. moduleauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

"""


class Base:
    """Crafty base operations.  :ref:`base`

    :param w: The width of crafty window
    :param h: The height of crafty window
    :param stage: An element to which this window will be attached
    :returns: An instance of Crafty
    """
    def __init__(self, crafty):
        """Crafty game engine constructor.

        :param crafty: An element to which this window will be attached
        :returns: An instance of Crafty
        """
        self.__crafty = crafty
        #crafty.attr(self=self)

    def attr(self, **kwarg):
        """Set attributes.  :mod:`crafty.entity`

        :param: kwargs: keyword parameters with name and values of arguments to be changed
        :returns: Self, this same entity
        """
        #print(kwarg)
        self.__elt.attr(dict(**kwarg))
        return self

    def background(self, color):
        """Change background color. :class:`crafty.base.Base`

        :param color: A string with components ex:'2D, DOM, Color'
        :returns: This instance of Crafty
        """
        self.__crafty.background(color)
        return self

    @property
    def x(self):
        """The x position on the stage. :class:`crafty.base.Base`

        """
        return self.__crafty.x

    @property
    def y(self):
        """The y position on the stage. :class:`crafty.base.Base`

        """
        return self.__crafty.y

    @property
    def mousePos(self):
        """Mouse Position. :class:`crafty.base.Base`

        """
        return self.__crafty.mousePos

    @property
    def keys(self):
        """Keycodes. :class:`crafty.base.Base`

        exemple keys.RA keys.LA keys.UA keys. DA

        """
        return self.__crafty.keys

    def isDown(self, keyName):
        """Determine if a certain key is currently down. :class:`crafty.base.Base`

        **Example**

        .. code-block:: python

            entity.requires('Keyboard').bind('KeyDown', haldle_keydown)

        Determine if a certain key is currently down.
        :param keyName: Name or Code of the key to check. See Crafty.keys.
        :returns: If the key is Down.
        """
        return self.__crafty.isDown(keyName)

    def crafty(self):
        """Crafty js core. :class:`crafty.base.Base`

        :returns: A javascript crafty instance
        """
        return self.__crafty

    def text(self, texty):
        """Crafty Text. :class:`crafty.base.Base`

        String of text that will be inserted into the DOM or Canvas element.

        This method will update the text inside the entity.

        If you need to reference attributes on the entity itself you can pass a function instead of a string.
        Example

        Crafty.e("2D, DOM, Text").attr({ x: 100, y: 100 }).text("Look at me!!");

        Crafty.e("2D, DOM, Text").attr({ x: 100, y: 100 })
            .text(function () { return "My position is " + this._x });

        Crafty.e("2D, Canvas, Text").attr({ x: 100, y: 100 }).text("Look at me!!");

        Crafty.e("2D, Canvas, Text").attr({ x: 100, y: 100 })
            .text(function () { return "My position is " + this._x });

        :param text: Name of the event to bind to
        :returns: Load a crafty scene
        """
        print('Crafty Text. Text')
        self.__crafty.requires('Text')
        self.__crafty.text(texty)
        return self

    def textColor(self, color):
        """Change the color of the text. You can use HEX, rgb and rgba colors.

        :param color: The color in name, hex, rgb or rgba
        :return: Self, this same entity
        """
        self.__crafty.textColor(color)
        return self

    def textFont(self, size="10px", weight="normal", face="normal", family="Arial"):
        """Use this method to set font property of the text entity.

        :param size: Size of the font in pixels ex: "20px"
        :param weight: Weight o font ex: "bold"
        :param face: Type of fonte ex: "italic"
        :param family: Font family
        :return: Self, this same entity
        """
        self.__crafty.textFont(dict(size=size, weight=weight, type=face, family=family))
        return self

    def unselectable(self):
        """This method sets the text so that it cannot be selected (highlighted) by dragging.

        :return: Self, this same entity
        """
        self.__crafty.unselectable()
        return self

    def bind(self, eventName, callback):
        """Crafty Bind. :class:`crafty.base.Base`

        Binds to a global event. Method will be executed when Crafty.trigger is used with the event name.

        :param eventName: Name of the event to bind to
        :param callback: Method to execute upon event triggered
        :returns: callback function which can be used for unbind
        """
        return self.__crafty.bind(eventName, callback)

    def onebind(self, eventName, callback):
        """Crafty OneBind. :class:`crafty.core.BCrafty`

        Binds to a global event. Method will be executed once when Crafty.trigger is used with the event name.

        :param eventName: Name of the event to bind to
        :param callback: Method to execute upon event triggered
        :returns: callback function which can be used for unbind
        """
        return self.__crafty.one(eventName, callback)

    def unbind(self, eventName, callback):
        """Crafty unbind. :class:`crafty.core.BCrafty`

        Binds to a global event. Method will be executed once when Crafty.trigger is used with the event name.

        :param eventName: Name of the event to unbind to
        :param callback: Method to unbind
        :returns: True or false depending on if a callback was unbound
        """
        return self.__crafty.unbind(eventName, callback)

    def destroy(self):
        """Destroy the Entity. :class:`crafty.core.BCrafty`
        Will remove all event listeners and delete all properties as well as removing from the stage

        :returns: The object destroyied
        """
        return self.__crafty.destroy()


class ViewPort:
    """Viewport is essentially a 2D camera looking at the stage.
    Can be moved or zoomed, which in turn will react just like a camera moving in that direction.  :ref:`draggable`

    """
    def __init__(self, ent):
        self.__ent = ent.viewport

    @property
    def clampToEntities(self):
        """Decides if the viewport functions should clamp to game entities.
        When set to true functions such as Crafty.viewport.mouselook() will not allow you to move
        the viewport over areas of the game that has no entities. For development it can be useful to set this to false.

        :return: True if clamped
        """
        return self.__ent.clampToEntities

    @clampToEntities.setter
    def clampToEntities(self, boolean):
        """Decides if the viewport functions should clamp to game entities.
        When set to true functions such as Crafty.viewport.mouselook() will not allow you to move
        the viewport over areas of the game that has no entities. For development it can be useful to set this to false.

        :param bool: Set to clamp if True
        """
        self.__ent.clampToEntities = boolean

    @property
    def x(self):
        """Will move the stage and therefore every visible entity along the x axis in the opposite direction.

        :return: viewport x
        """
        return self.__ent.x

    @x.setter
    def x(self, position):
        """When this value is set, it will shift the entire stage. This means that entity positions are not exactly
         where they are on screen. To get the exact position, simply add Crafty.viewport.x onto the entities x position.

        :param position: Set the viewport x position
        """
        self.__ent.x = position

    @property
    def y(self):
        """Will move the stage and therefore every visible entity along the x axis in the opposite direction.

        :return: viewport y
        """
        return self.__ent.y

    @y.setter
    def y(self, position):
        """When this value is set, it will shift the entire stage. This means that entity positions are not exactly
         where they are on screen. To get the exact position, simply add Crafty.viewport.y onto the entities y position.

        :param position: Set the viewport y position
        """
        self.__ent.y = position

    @property
    def _scale(self):
        """This value is the current scale (zoom) of the viewport. When the value is bigger than 1,
        everything looks bigger (zoomed in). When the value is less than 1, everything looks smaller (zoomed out).
        This does not alter the size of the stage itself, just the magnification of what it shows.


        :return: the current scale (zoom) of the viewport
        """
        return self.__ent._scale

    def bounds(self, minx, miny, maxx, maxy):
        """A rectangle which defines the bounds of the viewport.

        :param minx: min x bound of viewport
        :param miny: min y bound of viewport
        :param maxx: max x bound of viewport
        :param maxy: max y bound of viewport
        :returns: Self, this same entity
        """
        self.__ent.bounds = dict(min=dict(x=minx, y=miny), max=dict(x=maxx, y=maxy))
        return self

    def scroll(self, axis, val):
        """Will move the viewport to the position given on the specified axis

        :param axis: 'x' or 'y'
        :param val: The new absolute position on the axis
        :returns: Self, this same entity
        """
        self.__ent.scroll(axis, val)
        return self

    def pan(self, dx, dy, time):
        """Pans the camera a given number of pixels over the specified time

        :param dx: The distance along the x axis
        :param dy: The distance along the y axis
        :param time: The duration in ms for the entire camera movement
        :returns: Self, this same entity
        """
        self.__ent.pan(dx, dy, time)
        return self

    def follow(self, target, offsetx=0, offsety=0):
        """Follows a given entity with the 2D component. If following target will take a portion of the viewport
        out of bounds of the world, following will stop until the target moves away.

        :param target: An entity with the 2D component
        :param offsetx: Follow target should be offsetx pixels away from center
        :param offsety: Positive puts target to the right of center
        :returns: Self, this same entity
        """
        self.__ent.follow(target.entity, offsetx, offsety)
        return self

    def centerOn(self, target, time):
        """Centers the viewport on the given entity.

        :param target: An entity with the 2D component
        :param time: The duration in ms of the camera motion
        :return: Self, this same entity
        """
        self.__ent.centerOn(target.entity, time)
        return self

    def zoom(self, amt, cent_x, cent_y, time):
        """Zooms the camera in on a given point. amt > 1 will bring the camera closer to the subject
        amt < 1 will bring it farther away. amt = 0 will reset to the default zoom level Zooming is multiplicative.
        To reset the zoom amount, pass 0.

        :param amt: amount to zoom in on the target by (eg. 2, 4, 0.5)
        :param cent_x: the center to zoom on
        :param cent_y: the center to zoom on
        :param time: the duration in ms of the entire zoom operation
        :return: Self, this same entity
        """
        self.__ent.zoom(amt, cent_x, cent_y, time)
        return self

    def scale(self, amt):
        """Adjusts the scale (zoom). When amt is 1, it is set to the normal scale, e.g.
        an entity with this.w == 20 would appear exactly 20 pixels wide.
        When amt is 10, that same entity would appear 200 pixels wide (i.e., zoomed in by a factor of 10),
        and when amt is 0.1, that same entity would be 2 pixels wide (i.e., zoomed out by a factor of (1 / 0.1)).

        If you pass an amt of 0, it is treated the same as passing 1, i.e. the scale is reset.

        This method sets the absolute scale, while Crafty.viewport.zoom sets the scale relative to the existing value.


        :param amt: amount to zoom in on the target by (eg. 2, 4, 0.5)
        :return: Self, this same entity
        """
        self.__ent.scale(amt)
        return self

    def mouselook(self, boolean=True):
        """Toggle mouselook on the current viewport. Simply call this function
        and the user will be able to drag the viewport around.

        If the user starts a drag, "StopCamera" will be triggered, which will cancel any existing camera animations.

        :param boolean: Activate or deactivate mouselook
        :return: Self, this same entity
        """
        self.__ent.mouselook(boolean)
        return self

    def init(self, width, height, stage_elem):
        """Initialize the viewport. If the arguments 'width' or 'height' are missing, use Crafty.DOM.window.width
        and Crafty.DOM.window.height (full screen model).

        The argument 'stage_elem' is used to specify a stage element other than the default,
        and can be either a string or an HTMLElement. If a string is provided, it will look for an element
        with that id and, if none exists, create a div. If an HTMLElement is provided, that is used directly.
        Omitting this argument is the same as passing an id of 'cr-stage'.

        :param width: Width of the viewport
        :param height: Height of the viewport
        :param stage_elem: the element to use as the stage (either its id or the actual element).
        :return: Self, this same entity
        """
        self.__ent.init(width, height, stage_elem)
        return self
