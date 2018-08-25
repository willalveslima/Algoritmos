import Grafo

def singleSourceShortest(G,s):
    PQ =[]
    INF = 999999
    pred = [None] * G.V
    dist = [None] * G.V
    visited = [None] * G.V
    for v in range(G.V):
        dist[v] = INF
        pred[v] = -1
        visited[v] = False
    dist[s] = 0
    
    while True:
        u = -1
        tmp = INF
        for i in range(G.V):
            if visited[i] is False:
                if dist[i] < tmp:
                    tmp = dist[i]
                    u = i
                   

        if u == -1:
            break
        visited[u] = True
        for v in G.adj[u]:
                w = G.peso[(u,v)]
                newLen = dist[u] + w
                if newLen < dist[v]:
                    dist[v] = newLen
                    pred[v] = u
    for v in range(G.V):
        print('v {} - dist :{} - pred :{}'.format(v,dist[v],pred[v]))