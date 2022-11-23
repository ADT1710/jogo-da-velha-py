import math
import random

class Jogador:
    def __init__(self,letra):
        # Letra é X ou O
        self.letra = letra

    def pega_movimento(self, game):
        pass

class JogadorComputador(Jogador):
    def __init__(self,letra):
        super().__init__(letra)

    def pega_movimento(self, game):
        pass

class JogadorHumano(Jogador):
    def __init__(self, letra):
        super().__init__(letra)

    def pega_movimento(self, game):
        pass