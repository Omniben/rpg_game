import random


class Sigilo:
    sigilo = True

    def __init__(self, sigilo=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sigilo = sigilo

    def esconderse(self, nivel_de_luz):
        return self.sigilo and nivel_de_luz < 10


class Agil:
    agil = True

    def __init__(self, agil=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.agil = agil

    def evadir(self):
        return self.agil and bool(random.randint(0, 1))