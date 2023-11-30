import heapq
import networkx as nx
# RUN  "pip install networkx" in console if you don't have it it installed already
import matplotlib.pyplot as plt
import numpy as np


# Adjacency List Graph
class Adj_List_Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = {vertex: [] for vertex in range(vertices)} # adjacency list that is of size vertices

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # Assuming undirected/bidirectional graph

    # print out the dictionary holding the graph
    def print_graph(self):
        print(self.graph)
    
    # Ouputs an image of the graph
    # If you're too lazy to install the nx thingy just comment out ayyy
    def visualize(self):
        G = nx.Graph()

        # Add edges and edge weights to graph
        for vertex in self.graph:
            for neighbor, weight in self.graph[vertex]:
                G.add_edge(vertex, neighbor, weight=weight)

        # Set up the layout of graph
        pos = nx.spring_layout(G)
        # Create dictionary of edge labels for weights in graph
        labels = {(i, j): f"{weight}" for i, j, weight in G.edges.data("weight")}
        # Draw the graph with node labels
        nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=8)
        # Draw edge labels
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color='red')
        # Show the graph
        plt.show()
    
# Dijkstra with Adjacency List and Minimizing Heap as priority queue
def djikstra_AL(G, source, size):
    Q = [] # priority queue
    V = size  # assuming G.V gives number of vertices
    d = []
    pi = []
    for x in range(V):
        d.append(np.inf)
        pi.append(None)

    d[source] = 0
    heapq.heappush(Q, (0, source))
    while Q:
        md, u = heapq.heappop(Q) # md is minimum distance of the smallest vertex
        for v, weight in G.graph[u]: # need to create G as Graph_Adjacency(G) for this to work
            if d[v] > d[u] + weight:
                d[v] = d[u] + weight
                pi[v] = u
                heapq.heappush(Q, (d[v], v))
    return d


class Adj_Matrix_Graph(object):
    
    # Initialize the matrix
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size
        self.V=self.size

    # Add edges with weight
    def add_edge(self, v1, v2,weight):
        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
        self.adjMatrix[v1][v2] = weight # To make it directed make it unsymmetrical, V1->V2 (points to), weight stored in position
        #self.adjMatrix[v2][v1] = weight

    # Remove edges
    def remove_edge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            print("No edge between %d and %d" % (v1, v2))
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def __len__(self):
        return self.size

    # Print the matrix
    def print_matrix(self):
        i=0
        while i< self.size:
            print(self.adjMatrix[i])
            i+=1

    def visualize(self):
        G = nx.Graph()

        size = len(self.adjMatrix)

        # Add edges and edge weights to the graph
        for i in range(size):
            for j in range(size):
                if self.adjMatrix[i][j] != 0:
                    G.add_edge(i, j, weight=self.adjMatrix[i][j])

        # Set up the layout of graph
        pos = nx.spring_layout(G)
        # Create dictionary of edge labels for weights in graph
        labels = {(i, j): f"{weight}" for i, j, weight in G.edges.data("weight")}
        # Draw the graph with node labels
        nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=8)
        # Draw edge labels
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color='red')
        # Show the graph
        plt.show()


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
    if len(Q) == 0:
        return True
    else:
        return False

# Dijkstra with Adjacency Matrix and array as priority queue
def djikstra_AM(G, source, V):
    Q = [] # priority queue
    d = []
    pi = []
    for x in range(V):
        d.append(np.inf)
        pi.append(None)
    
    S = np.zeros(V)  # creates list of size V with all 0s
    d[source] = 0

    for v in range(V):  # put vertices in priority queue in increasing d[v] order
        Q.append((v, d[v]))  # [0] is vertex. [1] is weight of vertex

    while not isQEmpty(Q):
        u = getMin(Q)
        current_node = u[0]
        S[current_node] = 1
        Q.remove(u) # remove minimum value from Q

        for v in range(V):
            if v != current_node and G[current_node][v] != 0:  # not itself and neighbour
                if S[v] != 1 and d[v] > (d[current_node] + G[current_node][v]):
                    Q.remove((v, d[v]))
                    d[v] = d[current_node] + G[current_node][v]
                    pi[v] = current_node
                    Q.append((v, d[v]))
    return d

# Example graph
size = 100
g_list = Adj_List_Graph(size) # Adj List Graph, uncomment to try out
g_list = Adj_Matrix_Graph(size) # Adj Matrix Graph
g_list.add_edge(0, 1, 4)
g_list.add_edge(0, 2, 2)
g_list.add_edge(1, 2, 5)
g_list.add_edge(1, 3, 10)
g_list.add_edge(2, 3, 3)
g_list.add_edge(3, 4, 7)
#g_list.add_edge(15,16,5)

# Dik man power
start_vertex = 0

shortest_distances = djikstra_AL(g_list, start_vertex, size) # Adjacency List version

#shortest_distances = djikstra_AM(g_list.adjMatrix, start_vertex, size) # Adjacency Matrix version
print(f"Shortest distances from vertex {start_vertex}: {shortest_distances}")

# Wow it many numbar
# Format = (Node: [(Neighbor, Weight), (Neighbor, Weight), ...])
print("The graph representation in dictionary form:")
print(g_list.print_graph()) # Uncomment to print out adjacency list graph implementation
#print(g_list.print_matrix())

# Output image of graph
# Comments out if you laze install -_-
g_list.visualize()

