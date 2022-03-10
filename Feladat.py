class Feladat:

    def __init__(self, kezdo, cel = None):
        self.kezdo = kezdo
        self.cel = cel

    def celteszt(self, allapot):
        raise NotImplementedError

    def rakovetkezo(self, allapot):
        raise NotImplementedError
