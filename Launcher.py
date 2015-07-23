import pyglet
from pyglet.window import key

import cocos
from cocos import layer
from Character import *

# Singleton init

pyglet.resource.path.append(pyglet.resource.get_script_home())
pyglet.resource.reindex()


def main():
    import Singleton  # importation en écriture
    from cocos.director import director
    director.init(width=1024, height=768, autoscale=False)

    Singleton.keyboard = key.KeyStateHandler()
    # create a layer to put the player in
    character_layer = layer.ScrollableLayer()
    # NOTE: the anchor for this sprite is in the CENTER (the cocos default)
    # which means all positioning must be done using the center of its rect
    player = Player('sprites/units/characterM83.png')
    ennemy = IACharacter('sprites/units/character.png')
    character_layer.add(player)
    character_layer.add(ennemy)
    # player.do(PlayerController())
    # ennemy.do(BasicEnnemyController())

    # add the tilemap and the player sprite layer to a scrolling manager
    Singleton.scroller = layer.ScrollingManager()

    # spacebackground = tiles.load_tmx('MapTile01.tmx')['background']
    Singleton.tilemap = tiles.load_tmx('MapTile01.tmx')['middle']

    # scroller.add(spacebackground, z=0)
    Singleton.scroller.add(Singleton.tilemap, z=1)
    Singleton.scroller.add(character_layer, z=2)

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
    platformer_scene.add(Singleton.scroller, z=1)

    # track keyboard presses

    director.window.push_handlers(Singleton.keyboard)

    # run the scene
    director.run(platformer_scene)


if __name__ == '__main__':
    main()
