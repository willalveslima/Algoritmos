#----------------------------------------------------
# Deapth First Search                            
# Implementaçao em Python do Algoritmo Deapth First Search 
# Presente no livro Algoritmos  O Guia Essencial
# de Heineman, Pollice e Selkow
# Versao 0.1 
# Data 21/08/2018
#-----------------------------------------------------

import Grafo

def Search(G,s):
    d = f = pred = [None] * G.V
    
    for v in range(G.V):
        d[v] = f[v] = pred[v] = -1
        
        G.nodeColor[v] = 'white'
    counter = 0
    G.plot()
    dfs_visit(s,G,d,f,pred,counter)
    G.plot()
    for v in range(G.V):
        if G.nodeColor[v] == 'white':
            dfs_visit(v,G,d,f,pred,counter)
    G.plot        
def dfs_visit(u,G,d,f,pred,counter):
    G.nodeColor[u] = 'Gray'
    d[u] = ++counter
    for v in G.adj[u]:
        if G.nodeColor[v] == 'white':
            pred[v] = u
            dfs_visit(v,G,d,f,pred,counter)
    G.nodeColor[u] = 'black'    
    f[u] = ++counter