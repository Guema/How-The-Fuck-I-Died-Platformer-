import cocos
import pyglet


class Weapon():

    """
        this class allow to fire bullets lol
    """

    def __init__(self, model, maxrange, damages, speed):
        self.model = model  # is a cocos.sprite
        self.range = maxrange
        self.damages = damages  # is an integer
        self.speed = speed  # is a float ?

    def Fire(self):
        """
            this method fire a bullet
        """
