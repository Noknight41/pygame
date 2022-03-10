import numpy as np

dimesion = 2

class Node:
    def __init__(self, size, data, row, column, block):
        self.m = size
        self.data = data
        self.row = row
        self.column = column
        self.block = block
            
    def addTo(self, value, i, j):
        if value > 0 and value < self.m * self.m + 1:
            self.data[i][j] = value
            self.row[i].remove(value)
            self.column[j].remove(value)
            self.block[ (i // self.m) * self.m + j // self.m ].remove(value)
        
    def preChecking(self):
        for i in range(0, self.m * self.m):
            for j in range(0, self.m * self.m):
                if self.data[i][j] != '_':
                    t = self.data[i][j]
                    self.addTo(t, i, j)
    
    def legalValue(self, value, i, j):
        return value in self.row[i] and value in self.column[j] and value in self.block[ (i // self.m) * self.m + j // self.m ]
        
    def printNode(self):
        print(self.data)

class Sudoku:
    def __init__(self,size):
        self.m = size
        self.n = size * size

    def accept(self):
        puz = []
        for i in range(0, self.n):
            temp = input().split(" ")
            puz.append(temp)
        return puz

    def process(self):
        self.fill(0, 0, self.start)
        self.solution.printNode()
        
    def fill(self, i, j, node):
        if node.data[i][j] == 0:
            for value in range(1, self.n + 1):
                if node.legalValue(value, i, j):
                    new_node = Node(node.m, node.data, node.row, node.column, node.block)
                    new_node.addTo(value, i, j)
                    if j == self.n - 1:
                        if i == self.n - 1:
                            self.solution = new_node
                        else:
                            self.fill(i + 1, 0, node)
                    else:
                        self.fill(i, j + 1, node)
        else:
            if j == self.n - 1:
                if i == self.n - 1:
                    self.solution = node
                else:
                    self.fill(i + 1, 0, node)
            else:
                self.fill(i, j + 1, node)
    
    def load(self, path):
        # Load a configuration to solve.
        with open(path, "r") as f:
            values = np.loadtxt(f).reshape((self.m * self.m, self.m * self.m)).astype(int)
            print(values)
            r = []
            c = []
            b = []
            for i in range(0, self.n):
                r.append(list(range(1, self.n + 1)))
                c.append(list(range(1, self.n + 1)))
                b.append(list(range(1, self.n + 1)))
            self.start = Node(self.m , values, r, c, b)
        return            
    
    def run(self):
        self.start.preChecking()
        self.process()

puz = Sudoku(dimesion)
start = [[0,4,0,0], [0,0,0,4], [3,0,0,0], [0,2,0,0]]
puz.load("test1.txt")
puz.run()