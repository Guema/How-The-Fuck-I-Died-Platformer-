"""TODO"""
import cocos
import pyglet
from cocos.actions import *


class HelloWorld(cocos.layer.ColorLayer):

    """TODO"""

    def __init__(self):
        """TODO"""
        super(HelloWorld, self).__init__(64, 64, 224, 255)


class KeyDisplay(cocos.layer.Layer):

    is_event_handler = True

    def __init__(self):
        super(KeyDisplay, self).__init__()
        self.text = cocos.text.Label("", x=100, y=200)

        self.keys_pressed = set()
        self.update_text()
        self.add(self.text)

    def update_text(self):

        key_names = [pyglet.window.key.symbol_string(k)
                     for k in self.keys_pressed]
        text = 'Keys: ' + ','.join(key_names)
        # Update self.text
        self.text.element.text = text

    def on_key_press(self, key, modifiers):
        """This function is called when a key is pressed.
        'key' is a constant indicating which key was pressed.
        'modifiers' is a bitwise or of several constants indicating which
        modifiers are active at the time of the press
        (ctrl, shift, capslock, etc.)
        """
        self.keys_pressed.add(key)
        self.update_text()

    def on_key_release(self, key, modifiers):
        """This function is called when a key is released.

        'key' is a constant indicating which key was pressed.
        'modifiers' is a bitwise or of several constants indicating which
        modifiers are active at the time of the press
        (ctrl, shift, capslock, etc.)

        Constants are the ones from pyglet.window.key
        """

        self.keys_pressed.remove(key)
        self.update_text()

cocos.director.director.init()
hello_layer = KeyDisplay()

# sprite = cocos.sprite.Sprite('sprites/character.png')
# sprite.position = 320, 240
# sprite.scale = 3
# hello_layer.add(sprite)

main_scene = cocos.scene.Scene(hello_layer)
cocos.director.director.run(main_scene)
