#----------------------------------------------------
# Breadth-First Search                            
# Implementaçao em Python do Algoritmo Breadth-First Search 
# Presente no livro Algoritmos  O Guia Essencial
# de Heineman, Pollice e Selkow
# Versao 0.1 
# Data 22/08/2018
#-----------------------------------------------------

import Grafo

def Search(G,s):
    dist = pred = [None] * G.V
    
    for v in range(G.V):
        pred[v] = -1
        G.nodeColor[v] = 'white'
    G.nodeColor[s] = 'gray'
    dist[s] = 0
    Q = []
    Q.append(s)
    G.plot()

    while len(Q) > 0:
        u = Q.pop()
        for v in G.adj[u]:
            if G.nodeColor[v] == 'white':
                dist[v]= dist[u] + 1
                pred[v] = u
                G.nodeColor[v] = 'gray'
                Q.append(v)
        
        G.nodeColor[u] = 'black'
    G.plot()
    