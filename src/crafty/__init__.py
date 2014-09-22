#! /usr/bin/env python
# -*- coding: UTF8 -*-
"""
############################################################
Brython Crafty - INIT
############################################################

:Author: *Carlo E. T. Oliveira*
:Contact: carlo@nce.ufrj.br
:Date: 2014/09/17
:Status: This is a "work in progress"
:Revision: 0.1.0
:Home: `Labase <http://labase.selfip.org/>`__
:Copyright: 2013, `GPL <http://is.gd/3Udt>`__.

.. moduleauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

.. _mod_crafty

"""
from .core import BCrafty


class Crafty(BCrafty):
    """Crafty game engine main class.  :ref:`crafty`

    """
    pass


def main():
    from browser import document

    def bcrafty():
        #crafty = JSObject(Crafty)
        crafty = Crafty(500, 350, document['game'])
        #crafty.init(500,350, document['game']);
        #crafty.e('2D, DOM, Color').attr(dict(x= 0, y= 0, w= 100, h= 100)).color('#F00');
        crafty.e('Floor, 2D, Canvas, Color').attr(x=0, y=250, w=250, h=10).color('green')
        # crafty.e('2D, DOM, Color').attr(x=0, y=0, w=100, h=100)\
        #     .color('#F00').fourway(4).gravity('Floor')
        cft = crafty.crafty
        #crafty.canvas.init()

        #turn the sprite map into usable components
        crafty.sprites(
            16, "sprite.png",
                grass1=[0, 0],
                grass2=[1, 0],
                grass3=[2, 0],
                grass4=[3, 0],
                flower=[0, 1],
                bush1=[0, 2],
                bush2=[1, 2],
                player=[0, 3]
        )

        def generateWorld():
            #generate the grass along the x-axis
            for i in range(25):
                #generate the grass along the y-axis
                for j in range(25):
                    grassType = crafty.randRange(1, 4)
                    crafty.e("2D, Canvas, grass%d" % grassType).attr(x=i * 16, y=j * 16)

                    #1/50 chance of drawing a flower and only within the bushes
                    if (i > 0) and (i < 24) and (j > 0) and (j < 19) and (crafty.randRange(0, 50) > 49):
                        crafty.e("2D, DOM, flower, SpriteAnimation")\
                            .attr(x=i * 16, y=j * 16)\
                            .reel("wind", 1000, 0, 1, 3).animate("wind", -1)
                        """
                            .animate("wind", 0, 1, 3)
                            .bind("enterframe", function() {
                                if(!this.isPlaying())
                                    this.animate("wind", 80);
                            });
                            """
            #create the bushes along the x-axis which will form the boundaries
            for i in range(25):
                crafty.e("2D, Canvas, wall_top, bush%d" % crafty.randRange(1, 2))\
                    .attr(x=i * 16, y=0, z=2)
                crafty.e("2D, DOM, wall_bottom, bush%d" % crafty.randRange(1, 2))\
                    .attr(x=i * 16, y=304, z=2)
            
            #create the bushes along the y-axis
            #we need to start one more and one less to not overlap the previous bushes
            for i in range(19):
                crafty.e("2D, DOM, wall_left, bush%d" % crafty.randRange(1, 2))\
                    .attr(x=0, y=i * 16, z=2)
                crafty.e("2D, Canvas, wall_right, bush%d" % crafty.randRange(1, 2))\
                    .attr(x=384, y=i * 16, z=2)

        # The loading screen that will display while our assets load
        def ld(a=0):
            def mn(a=0):
                print("load main")
                crafty.scene("main")  # /when everything is loaded, run the main scene
            # Load takes an array of assets and a callback when complete
            print("load loader")
            crafty.load("sprite.png", mn)
            # Black background with some loading text
            crafty.background("#000")
            crafty.e("2D, DOM, text").attr(w=100, h=20, x=150, y=120)
            '''\
                .text("Loading")\
                .css(text_align="center")'''
        crafty.scene("loading", ld)

        def main_go(a=0):
            generateWorld()
        crafty.scene("main", main_go)

        # Automatically play the loading scene
        crafty.scene("loading")

        #generateWorld()
        crafty.c('test', dict(init=lambda slf=None: print("comp test", slf)))
        crafty.e('test')

        class Cmo:
            def init(self, ou=None):
                print("class comp test", self, ou)
        a = Cmo()
        a_ = {str(k): getattr(a, k) for k in dir(a) if '__' not in k}
        crafty.c('clastest', a_)
        crafty.e('clastest')

    def crafty():
        from javascript import JSObject
        crafty = JSObject(Crafty)
        crafty.init(500, 350, document['game'])
        crafty.e('2D, DOM, Color').attr(dict(x=0, y=0, w=100, h=100)).color('#F00')  # .fourway(4)
        crafty.e('Floor, 2D, Canvas, Color').attr(dict(x=0, y=250, w=250, h=10)).color('green')
        crafty.canvas.init()
        #turn the sprite map into usable components
        cft.sprite(16, "sprite.png", {
            grass1: [0, 0],
            grass2: [1, 0],
            grass3: [2, 0],
            grass4: [3, 0],
            flower: [0, 1],
            bush1: [0, 2],
            bush2: [1, 2],
            player: [0, 3]
        })

        #crafty.e('2D, DOM, Color').attr(x=0, y=0, w=100, h=100).color('#F00').fourway(4)

    bcrafty()
