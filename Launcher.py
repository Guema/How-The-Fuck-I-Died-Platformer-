import pyglet
from pyglet.window import key

import cocos
from cocos import tiles, actions, layer

keyboard = key.KeyStateHandler()

pyglet.resource.path.append(pyglet.resource.get_script_home())
pyglet.resource.reindex()


class PlayerController(actions.Action, tiles.RectMapCollider):
    on_ground = True
    MOVE_SPEED = 200
    JUMP_SPEED = 500
    GRAVITY = -1500

    def start(self):
        # initial velocity
        self.target.velocity = (0, 0)

    def step(self, dt):
        global keyboard, tilemap, scroller
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
        global keyboard, tilemap, scroller
        dx, dy = self.target.velocity

        # using the player controls, gravity and other acceleration influences
        # update the velocity
        dx = (self.GoRight - self.GoLeft) * self.MOVE_SPEED * dt
        dy = dy + self.GRAVITY * dt
        if self.on_ground and self.GoJump:
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


def main():
    global keyboard, tilemap, scroller
    from cocos.director import director
    director.init(width=1024, height=768, autoscale=False)

    # create a layer to put the player in
    character_layer = layer.ScrollableLayer()
    # NOTE: the anchor for this sprite is in the CENTER (the cocos default)
    # which means all positioning must be done using the center of its rect
    player = cocos.sprite.Sprite('sprites/units/characterM83.png')
    ennemy = cocos.sprite.Sprite('sprites/units/character.png')
    character_layer.add(player)
    character_layer.add(ennemy)
    player.do(PlayerController())
    ennemy.do(BasicEnnemyController())

    # add the tilemap and the player sprite layer to a scrolling manager
    scroller = layer.ScrollingManager()

    # spacebackground = tiles.load_tmx('MapTile01.tmx')['background']
    tilemap = tiles.load_tmx('MapTile01.tmx')['middle']

    # scroller.add(spacebackground, z=0)
    scroller.add(tilemap, z=1)
    scroller.add(character_layer, z=2)

    # set the player start using the player_start token from the tilemap
    # start = tilemap.find_cells(player_start=True)[0]
    # r = player.get_rect()

    # align the mid bottom of the player with the mid bottom of the start cell
    # r.midbottom = start.midbottom

    # player image anchor (position) is in the center of the sprite
    # player.position = r.center
    player.position = (100, 200)
    ennemy.position = (500, 500)

    # construct the scene with a background layer color and the scrolling
    # layers
    platformer_scene = cocos.scene.Scene()
    platformer_scene.add(layer.ColorLayer(100, 120, 150, 255), z=0)
    platformer_scene.add(scroller, z=1)

    # track keyboard presses

    director.window.push_handlers(keyboard)

    # run the scene
    director.run(platformer_scene)


if __name__ == '__main__':
    main()
