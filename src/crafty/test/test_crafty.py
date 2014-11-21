#! /usr/bin/env python
# -*- coding: UTF8 -*-
"""
############################################################
Brython Crafty - Test
############################################################

:Author: *Carlo E. T. Oliveira*
:Contact: carlo@nce.ufrj.br
:Date: 2014/09/22
:Status: This is a "work in progress"
:Revision: 0.1.0
:Home: `Labase <http://labase.selfip.org/>`__
:Copyright: 2013, `GPL <http://is.gd/3Udt>`__.
"""
__author__ = 'carlo'
import unittest
import json
from unittest.mock import MagicMock, Mock, ANY, patch


class TestCrafty(unittest.TestCase):

    def setUp(self):
        """Pathes Brython document, JSObject, JSConstructor, __random and javascript Crafty module.
        """
        def return_javascript_module_crafty(obj):
            if obj == self.b_mock.JSCrafty:
                return self.c_mock
            return self.b_mock

        self.b_mock = MagicMock(name="brython")
        self.c_mock = MagicMock(name="javascrip_crafty")
        self.b_mock.JSObject = MagicMock(name="jsobject", side_effect=return_javascript_module_crafty)
        self.b_mock.JSCrafty = MagicMock(name="jscrafty", side_effect=return_javascript_module_crafty)
        modules = {
            'crafty.jscrafty': self.b_mock,
            'crafty.jscrafty.JSCrafty': self.b_mock.JSCrafty,
            '__random': self.b_mock,
            'browser': self.b_mock,
            'browser.document': self.b_mock,
            'javascript': self.b_mock,
            'javascript.JSObject': self.b_mock.JSObject,
            'javascript.JSConstructor': self.b_mock.JSConstructor
        }

        self.module_patcher = patch.dict('sys.modules', modules)
        self.module_patcher.start()
        from crafty import Crafty
        self.cft = Crafty()

    def tearDown(self):
        """Remove patches.
        """
        self.module_patcher.stop()

    def test_init(self):
        """initial creation."""
        self.b_mock.JSObject.assert_called_once_with(self.b_mock.JSCrafty)

    def test_background(self):
        """change background."""
        self.cft.background("red")
        self.c_mock.background.assert_called_once_with("red")

    def test_entity(self):
        """create entity."""
        from crafty.entity import Entity
        entity = self.cft.e('2D, DOM, Color')
        assert isinstance(entity, Entity), "Not entity but %s" % type(entity)
        self.c_mock.e.assert_called_once_with('2D, DOM, Color')

    def test_text(self):
        """create text."""
        entity = self.cft.text('2D, DOM, Color')
        self.c_mock.text.assert_called_once_with('2D, DOM, Color')

    def test_bind(self):
        """bind function."""
        func = lambda: None
        bound = self.cft.bind('Click', func)
        self.c_mock.bind.assert_called_once_with('Click', func)

    def test_component(self):
        """create component."""
        class Comp:
            def init(self):
                pass
        cmp = Comp()
        comp = self.cft.c('acomp', cmp)
        self.c_mock.c.assert_called_once_with('acomp', dict(init=cmp.init))

    def test_sprite(self):
        """create sprite."""
        from crafty.graphics import Sprite
        sprite = self.cft.sprite(1, 2, 3, 4)
        assert isinstance(sprite, Sprite), "Not sprite but %s" % type(sprite)
        self.c_mock.sprite.assert_called_once_with(1, 2, 3, 4)

    def test_tween(self):
        """tween an entity or sprite."""
        from crafty.graphics import Sprite
        sprite = self.cft.sprite(1, 2, 3, 4)
        sprite.tween(1000, rotation=90)
        self.c_mock.tween.assert_called_once_with({'rotation': 90}, 1000)
