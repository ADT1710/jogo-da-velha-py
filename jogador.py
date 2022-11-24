import math
import random
import jogo

class Jogador:
    def __init__(self,letra):
        # Letra é X ou O
        self.letra = letra

    def pega_movimento(self, jogo):
        pass

class JogadorComputador(Jogador):
    def __init__(self,letra):
        super().__init__(letra)

    def pega_movimento(self, jogo):
        quadrado = random.choice(jogo.movimentos_disponiveis())
        return quadrado

class JogadorHumano(Jogador):
    def __init__(self, letra):
        super().__init__(letra)

    def pega_movimento(self, jogo):
        quadrado_valido = False
        val = None
        while not quadrado_valido:
            quadrado = input(self.letra + "\ turno. Entre com um movimento (0-9): ")
            try:
                val = int(quadrado)
                if val not in jogo.movimentos_disponiveis():
                    raise ValueError
                quadrado_valido = True
            except ValueError:
                print('Quadrado inválido, tente novamente!')
        return val