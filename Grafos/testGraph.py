from Grafo  import igraph

grafo = Graph(9)

grafo.addEdge(0,1)
grafo.addEdge(0,4)
grafo.addEdge(1,2)
grafo.addEdge(1,0)
grafo.addEdge(2,1)
grafo.addEdge(2,6)
grafo.addEdge(4,0)
grafo.addEdge(4,5)
grafo.addEdge(4,3)
grafo.addEdge(3,4)
grafo.addEdge(3,2)
grafo.addEdge(8,7)
grafo.addEdge(7,8)

grafo.imprime_arestas()
