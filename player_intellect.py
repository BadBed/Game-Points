import fight


class PlayerIntellect(fight.FightObject):
    def __init__(self, player):
        super().__init__()
        self.player = player

    def event(self, fight, e):
        pass
