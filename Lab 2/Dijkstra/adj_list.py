import heapq
import networkx as nx
# RUN  "pip install networkx" in console if you don't have it it installed already
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = {vertex: [] for vertex in range(vertices)} # adjacency list that is of size vertices

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # Assuming undirected/bidirectional graph

    # print out the dictionary holding the graph
    def print_graph(self):
        print(self.graph)

    # Feel free to ignore this, chatgpt abit OP
    def dijkstra(self, start):
        visited = [False] * self.vertices
        distance = [float('inf')] * self.vertices # set as infinity
        distance[start] = 0

        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if visited[current_vertex]:
                continue

            visited[current_vertex] = True

            for neighbor, weight in self.graph[current_vertex]:
                new_distance = distance[current_vertex] + weight

                if new_distance < distance[neighbor]:
                    distance[neighbor] = new_distance
                    heapq.heappush(priority_queue, (new_distance, neighbor))

        return distance
    
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

# Example graph
g = Graph(5)
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 2)
g.add_edge(1, 2, 5)
g.add_edge(1, 3, 10)
g.add_edge(2, 3, 3)
g.add_edge(3, 4, 7)

# Dik man power
start_vertex = 0
shortest_distances = g.dijkstra(start_vertex)
print(f"Shortest distances from vertex {start_vertex}: {shortest_distances}")

# Wow it many numbar
# Format = (Node: [(Neighbor, Weight), (Neighbor, Weight), ...])
print("The graph representation in dictionary form:")
print(g.print_graph())

# Output image of graph
# Comments out if you laze install -_-
g.visualize()

