from grafo import Grafo
from adjacente import Adjacente

grafo = Grafo()

grafo.araraquara.adicionaadjacente(Adjacente(grafo.matao,33))
grafo.araraquara.adicionaadjacente(Adjacente(grafo.ibate,30))
grafo.araraquara.adicionaadjacente(Adjacente(grafo.gaviaopeixoto,34))
grafo.araraquara.adicionaadjacente(Adjacente(grafo.americobrasiliense,12))
grafo.araraquara.adicionaadjacente(Adjacente(grafo.buenodeandrada,15))

grafo.buenodeandrada.adicionaadjacente(Adjacente(grafo.,12))

grafo.matao.adicionaadjacente(Adjacente(grafo.dobrada,11))

grafo.ibate.adicionaadjacente(Adjacente(grafo.saocarlos,15))



grafo.araraquara.mostra_adjacentes()