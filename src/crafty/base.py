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

    def background(self, color):
        """Change background color. :class:`crafty.core.BCrafty`

        :param color: A string with components ex:'2D, DOM, Color'
        :returns: This instance of Crafty
        """
        self.__crafty.background(color)
        return self

    @property
    def mousePos(self):
        """Mouse Positiom. :class:`crafty.core.BCrafty`

        """
        return self.__crafty.mousePos

    def crafty(self):
        """Crafty js core. :class:`crafty.core.BCrafty`

        :returns: A javascript crafty instance
        """
        return self.__crafty

    def text(self, text):
        """Crafty Text. :class:`crafty.core.BCrafty`

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
        self.__crafty.text(text)
        return self

    def bind(self, eventName, callback):
        """Crafty Bind. :class:`crafty.core.BCrafty`

        Binds to a global event. Method will be executed when Crafty.trigger is used with the event name.

        :param eventName: Name of the event to bind to
        :param callback: Method to execute upon event triggered
        :returns: callback function which can be used for unbind
        """
        return self.__crafty.bind(eventName, callback)
