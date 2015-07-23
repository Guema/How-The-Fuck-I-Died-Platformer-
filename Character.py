import cocos


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


class IACharacter(Character):

    """
        This class is a special subclass for IA
        Controlled characeters
    """

    def __init__(self, path):
        super(IACharacter, self).__init__(path)
        # this statement call super constructor
