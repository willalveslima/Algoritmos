from Grafo  import Graph


grafo = Graph(9)
grafo.addEdge(0,1)
grafo.addEdge(0,4)
grafo.addEdge(1,2)
grafo.addEdge(2,1)
grafo.addEdge(2,6)
grafo.addEdge(4,0)
grafo.addEdge(4,5)
grafo.addEdge(4,3)
grafo.addEdge(3,2)
grafo.addEdge(8,7)


grafo.imprime_arestas()
print(grafo.connected())
grafo.plot()




