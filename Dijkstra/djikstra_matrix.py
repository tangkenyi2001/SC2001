import numpy as np


def getMin(s):
    length = len(s)
    minimum = s[0]
    if length == 1:
        return minimum
    else:
        for x in range(length):
            if s[x] < minimum:
                minimum = s[x]
        return minimum


def isQEmpty(Q):
    if Q.len() == 0:
        return 1
    else:
        return 0

# Dijkstra Adjacency Matrix with array as priority queue
def dijkstra_AM(G, source, V):  # V is number of vertices.
    Q = []  # priority queue
    d, pi = []
    for x in range(V):
        d[x] = np.inf
        pi[x] = None

    S = np.zeros(V)  # list of size V with all 0
    d[source] = 0

    for v in range(V):  # put vertices in priority queue in increasing d[v] order
        Q.append((v, d[v]))  # [0] is vertex. [1] is weight of vertex

    while not isQEmpty(Q):
        u = getMin(Q)
        current_node = u[0]
        S[current_node] = 1
        Q.remove(u)

        for v in range(V):
            if v is not u and G[current_node][v] is not None:  # not itself and neighbour
                if S[v] is not 1 and d[v] > d[current_node] + G[current_node][v]:
                    Q.remove((v, d[v]))
                    d[v] = d[current_node] + G[current_node][v]
                    pi[v] = current_node
                    Q.append((v, d[v]))