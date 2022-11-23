class JogoDaVelha:
    def __init__(self):
        self.tabuleiro = [" " for _ in range(9)]
        self.vencedor_atual = None

    def printa_tabuleiro(self):
        for linha in [self.tabuleiro[i * 3: (i + 1) * 3] for i in range(3)]:
            print("| " + " |".join(linha) + " |")

    @staticmethod
    def printa_numeros_tabuleiro():
        numero_tabuleiro = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for linha in numero_tabuleiro:
            print("| " + " |".join(linha) + " |")

    def movimentos_disponiveis(self):
        movimentos = []
        for (i,local) in enumerate(self.tabuleiro):
            if local == " ":
                movimentos.append(1)
        return movimentos