from Grafo  import Graph
import depthFirst
import breadthFirst
import dijkstraPQ
import dijkstraDG

grafo = Graph(9)
grafo.addEdge(0,1)
grafo.addEdge(0,4)
grafo.addEdge(4,0)
grafo.addEdge(4,5)
grafo.addEdge(4,3)
grafo.addEdge(3,4)
grafo.addEdge(3,2)
grafo.addEdge(2,1)
grafo.addEdge(2,6)
grafo.addEdge(6,2)
grafo.addEdge(8,7)
grafo.addEdge(7,8,10)

grafoD = Graph(5)
grafoD.addEdge(0,1,2)
grafoD.addEdge(0,4,4)
grafoD.addEdge(1,2,3)
grafoD.addEdge(2,4,1)
grafoD.addEdge(2,3,5)
grafoD.addEdge(4,3,4)
grafoD.addEdge(3,0,8)
'''
grafo.imprime_arestas()
print(grafo.connected())
grafo.plot()
print('*'*50)
print("depthFirst")
depthFirst.Search(grafo,0)
grafo.plot()
grafo.repintar()
grafo.plot()
print('*'*50)
print("breadthFirst")
breadthFirst.Search(grafo,0)
grafo.plot()
grafo.repintar()
grafo.plot()
'''
print('*'*50)
print("dijkstraPQ:")

#grafoD.plot()  
dijkstraPQ.singleSourceShortest(grafoD,0)
print("dijkstraDG:")
dijkstraDG.singleSourceShortest(grafoD,0)
