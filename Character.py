import cocos
from cocos import tiles, actions
from pyglet.window import key


class PlayerController(actions.Action, tiles.RectMapCollider):
    on_ground = True
    MOVE_SPEED = 200
    JUMP_SPEED = 500
    GRAVITY = -1500

    def start(self):
        # initial velocity
        self.target.velocity = (0, 0)

    def step(self, dt):
        # import singleton
        from Singleton import keyboard, tilemap
        dx, dy = self.target.velocity

        # using the player controls, gravity and other acceleration influences
        # update the velocity
        dx = (keyboard[key.RIGHT] - keyboard[key.LEFT]) * self.MOVE_SPEED * dt
        dy = dy + self.GRAVITY * dt
        if self.on_ground and keyboard[key.SPACE]:
            dy = self.JUMP_SPEED

        # get the player's current bounding rectangle
        last = self.target.get_rect()
        new = last.copy()
        new.x += dx
        new.y += dy * dt

        # run the collider
        dx, dy = self.target.velocity = self.collide_map(tilemap,
                                                         last,
                                                         new,
                                                         dy,
                                                         dx)
        self.on_ground = bool(new.y == last.y)

        # player position is anchored in the center of the image rect
        self.target.position = new.center

        # move the scrolling view to center on the player
        # scroller.set_focus(*new.center)


class BasicEnnemyController(actions.Action, tiles.RectMapCollider):
    on_ground = True
    MOVE_SPEED = 100
    JUMP_SPEED = 500
    GRAVITY = -1500

    def start(self):
        # initial velocity
        self.target.velocity = (0, 0)
        self.GoLeft = 1
        self.GoRight = 0
        self.GoJump = False

    def step(self, dt):
        # import singleton
        from Singleton import tilemap
        dx, dy = self.target.velocity

        # using the player controls, gravity and other acceleration influences
        # update the velocity
        dx = (self.GoRight - self.GoLeft) * self.MOVE_SPEED * dt
        dy = dy + self.GRAVITY * dt
        if self.on_ground and self.GoJump:
            dy = self.JUMP_SPEED
            cocos.actions.Rotate

        # get the player's current bounding rectangle
        last = self.target.get_rect()
        new = last.copy()
        new.x += dx
        new.y += dy * dt

        # run the collider
        dx, dy = self.target.velocity = self.collide_map(tilemap,
                                                         last,
                                                         new,
                                                         dy,
                                                         dx)
        self.on_ground = bool(new.y == last.y)

        # player position is anchored in the center of the image rect
        self.target.position = new.center

        # move the scrolling view to center on the player
        # scroller.set_focus(*new.center)


class Character(cocos.sprite.Sprite):

    """
        This class wrap methods to interract between characters
    """

    def __init__(self, path):
        super(Character, self).__init__(path)


class Player(Character):

    """
        This class is a special subclass for Player
    """

    def __init__(self, path):
        super(Player, self).__init__(path)
        # this statement call super constructor
        self.do(PlayerController())


class IACharacter(Character):

    """
        This class is a special subclass for IA
        Controlled characeters
    """

    def __init__(self, path):
        super(IACharacter, self).__init__(path)
        # this statement call super constructor
        self.do(BasicEnnemyController())
