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

IMG = "https://dl.dropboxusercontent.com/u/1751704/igames/img/"
SCENES = "eicamundo.jpg Fog04.png Foghole.png"
SPRITES = "treesprite.png fruit.png caveman.png largeemoji.png"
ti = 0
TT = []


def main():
    from browser import document
    from __random import randint


    class World:
        def __init__(self):
            self.crafty = crafty = Crafty(512, 512, document['game'])
            crafty.sprites(512, IMG+"eicamundo.jpg", mundo=[0, 0])
            crafty.sprites(512, IMG+"Fog04.png", fog=[0, 0])
            crafty.sprites(512, IMG+"Foghole.png", foghole=[0, 0])
            crafty.sprites(
                120, IMG+"treesprite.png",
                grass0=[0, 0],
                grass1=[1, 0],
                grass2=[2, 0],
                grass3=[3, 0],
                grass4=[0, 1],
                grass5=[1, 1],
                grass6=[2, 1],
                grass7=[3, 1],
            )
            fruits = {"fruit%d" % fr: [fr//3, fr % 3] for fr in range(12)}
            print(fruits)
            crafty.sprites(
                65, IMG+"fruit.png",**fruits)
            #crafty.e('2D, Canvas, Tween, fruit0').attr(x=300, y=100, w=30, h=30, _globalZ=40)
            #crafty.e('2D, Canvas, Tween, fruit11').attr(x=300, y=200, w=30, h=30, _globalZ=40)

            m = crafty.e('2D, Canvas, Tween, mundo').attr(alpha=1.0, x=0, y=0, w=512, h=512, _globalZ=10)
            self.foh = foh = crafty.e('2D, Canvas, Tween, foghole').attr(x=0, y=0, w=512, h=512, _globalZ=20)
            self.fog = fog = crafty.e('2D, Canvas, Mouse, Tween, fog')\
                .attr(alpha=0.95, x=0, y=0, w=512, h=512, _globalZ=30)
            fog.onebind("Click", self.clicked)
            fog.onebind("TweenEnd", self.showtrees)
            """
            self.fruitfall()
            """

        def clicked(self, ev=None):
            print('clickeed')
            self.fog.tween(3000, alpha=0.0)

        def fogfade(self):
            print('fogfade')
            self.foh.tween(3000, alpha=0.0)

        def fruitfall(self):
            print('fruitfall')
            #crafty.e('2D, Canvas, Tween, fruit0')
            for fruit in range(12):
                self.crafty.e('2D, Canvas, Tween, fruit%d' % fruit)\
                .attr(x=280 + 20*fruit//3, y=140+20*fruit % 3, w=16, h=16, _globalZ=40)\
                .tween(randint(100, 3000), y=140+10+20*fruit % 3 )

        def showtrees(self, ev=None):
            print('showtrees')
            for i in range(8):
                Tree(i, self.crafty, self)


    class Tree:
        TI = 0
        def __init__(self, i, crafty, world):
            print('Treeclickeed__init__', i)
            self.world = world
            self.i = i
            self._t = crafty.e('2D, Canvas, Mouse, Tween, grass%d' % i)\
                .attr(x=10 + 300*i//4, y=10+120*i % 4, w=100, h=100, _globalZ=100)
            self._t.bind("Click", self.click)
            self._click = self._position

        def click(self, i):
            self._click(i)

        def _position(self, i):
            print('Treeclickeed', Tree.TI)

            ti = Tree.TI
            dx, dy = randint(0,14), randint(0,14)
            self._t.tween(200, x=140+dx+25*ti//3, y=180+dx+25*ti % 3, w=20, h=20)
            Tree.TI += 1
            self._click = self._brake
            if Tree.TI >= 8:
                self.world.fogfade()

        def _brake(self, i):
            print('_brake', self.i)
            if self.i == 5:
                self.world.fruitfall()



    def ecrafty():
        World()

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
        crafty.c('clastest', a)
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
    def crafty_command():
        viewportWidth = 200
        viewportHeight = 200
        #Crafty.init(viewportWidth, viewportHeight)
        crafty = Crafty(viewportWidth, viewportHeight, document['game'])

        #Crafty.canvas.init();

        def iniscene(ev):
            def clicked(e=0, f=0):
                print(clicked, e, crafty, crafty.mousePos.x, clickText.text)
                clickText.text("Clicked:" + crafty.mousePos.x + ", " + crafty.mousePos.y)
            crafty.background("#ff0")
            clickText = crafty.e("2D, DOM, Text")\
                .attr(x=viewportWidth/4, y=180, w=150, h=40)\
                .text("Click somewhere")
            mouseTracker = crafty.e("2D, Mouse").attr(w=viewportWidth, h=viewportHeight, x=0, y=0)
            mouseTracker.bind("Click", clicked)
        crafty.scene("game", iniscene)
        crafty.scene("game")

    #crafty_command()
    ecrafty()
