import heapq

class Graph_Adjacency:  # Adjacency list
    def __init__(self, V):
        self.V = V
        self.adjList = [[] for _ in range(V)]

    def addEdge(self, u, v, weight):
        self.adjList[u].append((v, weight))
        self.adjList[v].append((u, weight))

# Dijkstra Adjacency Matrix with array as priority queue
def djikstra_AL(G, source):
    Q = [] # priority queue
    V = G.V  # assuming G.V gives number of vertices
    d, pi = []
    for x in range(V):
        d[x] = np.inf
        pi[x] = None

    d[source] = 0
    heapq.heappush(Q, (0, source))
    while Q:
        md, u = heapq.heappop(Q) # md is minimum distance of the smallest vertex
        for v, weight in G.adjList[u]: # need to create G as Graph_Adjacency(G) for this to work
            if d[v] > d[u] + weight:
                d[v] = d[u] + weight
                pi[v] = u
                heapq.heappush(Q, (d[v], v))