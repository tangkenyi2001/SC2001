

    for v in range(V):  # put vertices in priority queue in increasing d[v] order
        Q.append((v, d[v]))  # [0] is vertex. [1] is weight of vertex

    while not isQEmpty(Q):
        u = getMin(Q)