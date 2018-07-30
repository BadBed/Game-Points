ACTIVATE_ELEMENT = object()


class FightEvent(object):
    def __init__(self, type):
        self.type = type


class ActivateElement(FightEvent):
    def __init__(self, elem):
        super().__init__(ACTIVATE_ELEMENT)
        self.elem = elem