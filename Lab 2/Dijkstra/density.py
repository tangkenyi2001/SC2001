import heapq
import networkx as nx
# RUN  "pip install networkx" in console if you don't have it it installed already
import matplotlib.pyplot as plt
import numpy as np
import random
import time


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
timevalueslist=[]
timevaluesmatrix=[]
verticerange=[1000]
vertex_range = []
edge_range=[]
density_range=[]
for size in verticerange:
    timevalueslist=[]
    timevaluesmatrix=[]
    graphdensitylist=[]
    graphdensitymatrix=[]
    edge_range=[]
    g_list = Adj_List_Graph(size) # Adj List Graph, uncomment to try out
    g_matrix = Adj_Matrix_Graph(size) # Adj Matrix Graph
    edgesize=0
    for i in range(size-1): #min number of edges is x-1 generate matrix and list
        weight = random.randint(1, 10)  # Random edge weight
        g_list.add_edge(i, i + 1, weight)
        g_matrix.add_edge(i, i + 1, weight)
        edgesize+=1
    maxsize=size*(size-1)
    secondsize=maxsize-size
    counter=0
    for i in range(0,secondsize+2,10000):
        '''while counter<i:
            firstrandomvertex=random.randint(0, size-1)
            secondrandomvertex=random.randint(0, size-1)
            while firstrandomvertex == secondrandomvertex:
                secondrandomvertex = random.randint(0, size - 1)
            weight = random.randint(1, 10)
            if (g_matrix.adjMatrix[firstrandomvertex][secondrandomvertex]==0):
                g_list.add_edge(firstrandomvertex, secondrandomvertex, weight)
                g_matrix.add_edge(firstrandomvertex, secondrandomvertex, weight)
                edgesize+=1
                counter+=1'''
                
        start_vertex = 0
        #start=time.time()
        start = time.perf_counter()
        shortest_distanceslist = djikstra_AL(g_list, start_vertex, size) # Adjacency List version
        #end=time.time()
        end = time.perf_counter()
        #timetakenlist=end
        timetakenlist=(end-start)
        start = time.perf_counter()
        shortest_distancesmatrix = djikstra_AM(g_matrix.adjMatrix, start_vertex, size) # Adjacency Matrix version
        #end=time.time()
        end = time.perf_counter()
        #timetakenlist=end
        timetakenmatrix=(end-start)
        graphdensity=float(i/((size)*(size-1)))
        print(f"The time taken for list of size {size} against graph density {i}is {timetakenlist}")
        print(f"The time taken for matrix of size {size} against graph density is {timetakenmatrix}")
        graphdensitylist.append(timetakenlist)
        graphdensitymatrix.append(timetakenmatrix)
        #timevalueslist.append(timetakenlist)
        #timevaluesmatrix.append(timetakenmatrix)
        density_range.append(graphdensity)
        #vertex_range.append(size) 
        #edge_range.append(edgesize)
        
        #g_list.visualize()
        #g_matrix.visualize()
    #print(f"Shortest distances from vertex {start_vertex}: {shortest_distanceslist}")
    #print(f"Shortest distances from vertex {start_vertex}: {shortest_distancesmatrix}")
    # Format = (Node: [(Neighbor, Weight), (Neighbor, Weight), ...])
    plt.figure(figsize=(10,6))
    plt.plot(density_range, graphdensitylist, label='List Implementation', marker='o')
    plt.plot(density_range, graphdensitymatrix, label='Matrix Implementation', marker='x')
    plt.xlabel('Graph Density')
    plt.ylabel('Time Taken (seconds)')
    plt.title('Dijkstra Algorithm Performance')
    plt.grid(True)
    plt.legend()
    plt.show()
print(g_matrix.print_matrix)
print(timevalueslist)
print(timevaluesmatrix)
#print("The graph representation in dictionary form:")
#print(g_list.print_graph()) # Uncomment to print out adjacency list graph implementation
    #print(g_matrix.print_matrix())
    # Output image of graph
#g_list.visualize()
#g_matrix.visualize()

