# Adjacency Matrix representation in Python


class Graph(object):
    
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
        self.adjMatrix[v1][v2] = weight
        self.adjMatrix[v2][v1] = weight

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
    


def main():
    G = Graph(5)
    G.add_edge(0, 1, 3)
    G.add_edge(0, 2, 3)
    G.add_edge(1, 2, 4)
    G.add_edge(2, 0, 5)
    G.add_edge(2, 3, 9)

    G.print_matrix()


if __name__ == '__main__':
    main()
    