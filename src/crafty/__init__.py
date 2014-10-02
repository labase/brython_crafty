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
:Revision: 0.2.1
:Home: `Labase <http://labase.selfip.org/>`__
:Copyright: 2013, `GPL <http://is.gd/3Udt>`__.

.. moduleauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

.. _mod_crafty

"""
__version__ = "0.2.1"
from .core import BCrafty


class Crafty(BCrafty):
    """Crafty game engine main class.  :ref:`crafty`

    """
    pass

IMG = "https://dl.dropboxusercontent.com/u/1751704/igames/img/"
SPRITE_DIMENSIONS = dict(
    mundo=["eicamundo", 512, 1, 1], fog=["Fog04", 512, 1, 1], foghole=["Foghole", 512, 1, 1],
    tree=["treesprite", 120, 4, 8], fruit=["fruit", 65, 6, 12], caver=["caveman", 125, 5, 10],
    debris=["cacarecos", 32, 12, 48], emoji=["largeemoji", 47, 14, 4*14], baloon=["baloons", 600, 2, 2])
SPRITE_DIMENSIONS = [[key] + [value[0] + '.png']
                     + [it for it in value[1:]] for key, value in SPRITE_DIMENSIONS.items()]


def main():
    from browser import document, html
    from __random import randint, shuffle

    class World:
        def __init__(self):
            def cut_sprites(name, image, sprite_size, columns, total_pictures):
                spritenames = {
                    "%s%d" % (name, index): [index % columns, index//columns]
                    for index in range(total_pictures)}
                print(spritenames, image, sprite_size)
                crafty.sprites(sprite_size, IMG+image, **spritenames)
            self.talking = True
            self.talk = self._talk
            self.doc = document['game']
            print(SPRITE_DIMENSIONS)
            self.crafty = crafty = Crafty(512, 512, self.doc)
            [cut_sprites(*args) for args in SPRITE_DIMENSIONS]
            m = crafty.e('2D, Canvas, Tween, mundo0').attr(alpha=1.0, x=0, y=0, w=512, h=512, _globalZ=10)
            ''''''
            self.foh = foh = crafty.e('2D, Canvas, Tween, foghole0').attr(x=0, y=0, w=512, h=512, _globalZ=20)
            self.fog = fog = crafty.e('2D, Canvas, Mouse, Tween, Text, fog0')\
                .attr(alpha=0.95, x=0, y=0, w=512, h=512, _globalZ=30)
            self.ver = crafty.e('2D, Canvas, Tween, Text')\
                .attr(alpha=1.0, x=400, y=2, w=100, h=50, _globalZ=50).text("Version %s" % __version__)
            fog.onebind("Click", self.clicked)
            fog.onebind("TweenEnd", self.showtrees)
            ''''''
            self.ugh = ugh = Caveman(i=4, x=100, y=200, crafty=crafty, world=self)
            self.agh = agh = Caveman(i=6, x=240, y=265, crafty=crafty, world=self)
            """
            self.fruitfall()
            """
            #self.fogfade()

        def _notalk(self, ev=None):
            print('wo notalk')
            self.talking = not self.talking
            self.ugh.notalk(self.talking)
            self.agh.notalk(self.talking)

        def _talk(self, ev=None):
            print('wo talk')
            self.talk = self._notalk
            self.ugh.talk(None)
            self.agh.talk(None)

        def clicked(self, ev=None):
            print('clickeed')
            self.fog.tween(3000, alpha=0.0)

        def fogfade(self):
            print('fogfade')
            self.foh.tween(3000, alpha=0.0)
            debris = list(range(48))
            shuffle(debris)
            for drs, fig in enumerate(debris[:20]):
                Debris(drs, fig, self.crafty, self)

        def fruitfall(self):
            print('fruitfall')
            for fruit in range(12):
                self.crafty.e('2D, Canvas, Tween, fruit%d' % fruit)\
                    .attr(x=280 + 20*fruit//3, y=140+20*fruit % 3, w=16, h=16, _globalZ=14)\
                    .tween(randint(100, 3000), y=140+10+20*fruit % 3)

        def showtrees(self, ev=None):
            print('showtrees')
            for i in range(8):
                Tree(i, self.crafty, self)

        def matchdebris(self, debris):
            print('matchdebris')
            if Debris.TI < 12:
                debris.position(None)

    class Caveman:

        def __init__(self, i, x, y, crafty, world):
            print('Caveman __init__', i)
            self.world = world
            self.i = i
            self._b = None
            self.xy = (x, y)
            self.crafty = crafty
            self._t = crafty.e('2D, Canvas, Mouse, Tween, caver%d' % i)\
                .attr(x=x, y=y, w=25, h=25, _globalZ=17)
            self._t.bind("Click", self.click)
            self._talking = []

        def click(self, i):
            print('Caveman clickeed')
            self.world.talk(i)

        def notalk(self, talking=False):
            print('Caveman no_talk')
            self._b.visible = talking
            for lang in self._talking:
                lang.visible = talking

        def talk(self, i):
            print('Caveman clickeed')
            x, y = self.xy
            WR_OFF, WR_SZ = (self.i//5*130), (self.i//5*30)
            self._b = self.crafty.e('2D, Canvas, Tween, baloon%d' % (self.i//5))\
                .attr(x=x-100+WR_OFF, y=y-200, w=200+WR_SZ, h=200, _globalZ=18)
            self._talking = [
                self.crafty.e('2D, Canvas, Tween, emoji%d' % em)
                    .attr(x=x-75+WR_OFF + 55*em//3, y=y-180+40*em % 3+WR_SZ//2, w=38, h=38, _globalZ=19)
                for em in range(9)
            ]

        def move(self, x, y, action):
            print('Cavemanmove', x, y)
            self._t.tween(1000, x=x, y=y)
            self._t.onebind('TweenEnd', action)

    class Tree:
        TI = 0

        def __init__(self, i, crafty, world):
            print('Treeclickeed__init__', i)
            self.world = world
            self.i = i
            self._t = crafty.e('2D, Canvas, Mouse, Tween, tree%d' % i)\
                .attr(x=10 + 300*i//4, y=10+120*i % 4, w=100, h=100, _globalZ=100)
            self._t.bind("Click", self.click)
            self._click = self._position

        def click(self, i):
            self._click(i)

        def _position(self, i):
            print('Treeclickeed', Tree.TI)

            ti = Tree.TI
            dx, dy = randint(0, 14), randint(0, 14)
            self._t.tween(200, x=140+dx+25*ti//3, y=180+dx+25*ti % 3, w=20, h=20)
            Tree.TI += 1
            self._click = self._brake
            if Tree.TI >= 8:
                self.world.fogfade()

        def _brake(self, i):
            print('_brake', self.i)
            if self.i == 5:
                self.world.fruitfall()
                self._click = lambda ev=0: None

    class Debris:
        TI = 0

        def __init__(self, drs, fig, crafty, world):
            print('Treeclickeed__init__', i)
            self.world = world
            self.i = i
            dx, dy = randint(0, 20), randint(0, 10)
            self._t = crafty.e('2D, Canvas, Mouse, Tween, debris%d' % fig)\
                .attr(x=360+dx+16*drs//4, y=134+dy+16*drs % 4, w=16, h=16, _globalZ=15)

            self._t.bind("Click", self.click)

        def click(self, i):
            self.world.matchdebris(self)

        def position(self, i):
            print('Debris clickeed', Debris.TI)

            ti = Debris.TI
            dx, dy = randint(0, 5), randint(0, 5)
            self._t.tween(200, x=280+dx+16*ti//3, y=154+dx+16*ti % 3, w=16, h=16)
            Debris.TI += 1

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
            crafty.background("#ff0")
            clickText = crafty.e("2D, DOM, Text")\
                .attr(x=viewportWidth/4, y=180, w=150, h=40, alpha=0.0)\
                .text("Click somewhere")\
                .tween(3000, alpha=1.0).bind("TweenEnd", lambda x: clickText.attr(alpha=1.0))

            def clicked(e=0, f=0):
                print(clicked, e, crafty, crafty.mousePos.x, clickText, clickText.text)
                clickText.background("#0ff").text("Click elsewhere")
                #clickText.text("Click elsewhere")
                #clickText.text("Clicked:" + crafty.mousePos.x + ", " + crafty.mousePos.y)
          #clickText.text("Click elsewhere")
            mouseTracker = crafty.e("2D, Mouse").attr(w=viewportWidth, h=viewportHeight, x=0, y=0, alpha=0.0)
            mouseTracker.bind("Click", clicked)
        crafty.scene("game", iniscene)
        crafty.scene("game")

    #crafty_command()
    ecrafty()
