class Vertice:
    def __init__(self, rotulo):
        self.rotulo = rotulo
        self.visitado = False
        self.adjacentes = []

    def adicionaadjacente(self, adjacente):
        self.adjacentes.append(adjacente)

    def mostra_adjacentes(self):
        for adjacente in self.adjacentes:
            print(adjacente.vertice.rotulo, adjacente.custo)

