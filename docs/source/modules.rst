.. _crafty_module:

#######################
Core Module Description
#######################

.. seealso::

   Module :mod:`crafty`

.. note::
   Aggregates factory, control and interface units in this single module

.. _crafty:

Crafty
====================

Set of methods added to every single entity.

.. seealso::

   Class :class:`crafty.core.BCrafty`

.. note::
   Main API Unit.

.. _mod_entity:

#########################
Entity Module Description
#########################

.. seealso::

   Module :mod:`crafty.entity`

.. note::
   Aggregates entity and component in this single module

.. _entity:

Entity
====================

Creates an entity. Any arguments will be applied in the same way .addComponent() is applied as a quick way to add components.

Any component added will augment the functionality of the created entity by assigning the properties and methods from the component to the entity.

**Example**

.. code-block:: python

    myEntity = Crafty().e("2D, DOM, Color");

**Events**

*NewEntity [Data: { id:Number }]*
    When the entity is created and all components are added

See Also

.. seealso::

   Class :class:`crafty.entity.Entity`



.. note::
   Composite Element.

.. _mod_graphics:

###########################
Graphics Module Description
###########################

.. seealso::

   Module :mod:`crafty.graphics`

.. note::
   Aggregates canvas and sprite in this single module

.. _canvas:

Canvas
====================

When this component is added to an entity it will be drawn to the global canvas element. The canvas element (and hence all Canvas entities) is always rendered below any DOM entities.

Crafty.canvas.init() will be automatically called if it is not called already to initialize the canvas element.

Create a canvas entity like this

.. code-block:: python

    myEntity = Crafty().e("2D, Canvas, Color")\
         .color("green")\
         .attr(x= 13, y= 37, w= 42, h= 42);

**Events**

*Draw [Data: {type: "canvas", pos, co, ctx}]*
    when the entity is ready to be drawn to the stage
*NoCanvas*
    if the browser does not support canvas

.. seealso::

   Class :class:`crafty.graphics.Canvas`

.. note::
   DOm Element Unit.

.. _sprite:

Sprite
====================

Component for using tiles in a sprite map.

**Events**

*Invalidate*
    when the sprites change

.. seealso::

   Class :class:`crafty.graphics.Sprite`

.. note::
   Composite Unit.

Draggable
=========

Enable drag and drop of the entity.

**Events**

*Dragging* [Data: MouseEvent]
    is triggered each frame the entity is being dragged
*StartDrag* [Data: MouseEvent]
    is triggered when dragging begins
*StopDrag* [Data: MouseEvent]
    is triggered when dragging ends

.. seealso::

   Class :class:`crafty.graphics.Draggable`

.. note::
   Interface Unit.
