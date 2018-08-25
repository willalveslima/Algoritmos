import Grafo
import heapq

def singleSourceShortest(G,s):
    PQ =[]
    pred = [None] * G.V
    dist = [None] * G.V
    for v in range(G.V):
        dist[v] = 999999
        pred[v] = -1
    dist[s] = 0
    for v in range(G.V):
        heapq.heappush(PQ,[dist[v],v])
    while (PQ):
        u_h = heapq.heappop(PQ)
        u = u_h[1]
        if u_h[0] == dist[u]:
            for v in G.adj[u]:
                w = G.peso[(u,v)]
                newLen = dist[u] + w
                if newLen < dist[v]:
                    heapq.heappush(PQ, [ newLen,v])
                    dist[v] = newLen
                    pred[v] = u
    for v in range(G.V):
        print('v {} - dist :{} - pred :{}'.format(v,dist[v],pred[v]))