class Node:
    def __init__(self, data, level):
        """ Initialize the node with the data, level of the node and the calculated fvalue """
        self.data = data
        self.level = level
        self.solution = []
        
    def generate_child(self):
        """ Generate child nodes from the given node by moving the blank space
            either in the four directions {up,down,left,right} """
        x,y = self.find(self.data,'_')
        """ val_list contains position values for moving the blank space in either of
            the 4 directions [up,down,left,right] respectively. """
        val_list = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]
        children = []
        
        for i in val_list:
            child = self.shuffle_move(self.data, x, y, i[0], i[1])
            if child is not None:
                child_node = Node(child, self.level + 1)
                child_node.solution = self.solution + [self]
                children.append(child_node)
        return children
        
    def shuffle_move(self, puz, x1, y1, x2, y2):
        """ Move the blank space in the given direction and if the position value are out of limits the return None """
        if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data):
            temp_puz = []
            temp_puz = self.copy(puz)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            return temp_puz
        else:
            return None
        
    def copy(self, root):
        """ Copy function to create a similar matrix of the given node"""
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp    
            
    def find(self, puzzle, blank):
        """ Find the position of the blank space"""
        for i in range(0, len(self.data)):
            for j in range(0, len(self.data)):
                if puzzle[i][j] == blank:
                    return i,j
    
    def printMatrix(self):
        for i in self.data:
            for j in i:
                print(j, end=" ")
            print("")

class Puzzle:
    def __init__(self,size):
        """ Initialize the puzzle size by the specified size,open and closed lists to empty """
        self.n = size
        self.open = []
        self.closed = []
        
    def accept(self):
        """ Accepts the puzzle from the user """
        puz = []
        for i in range(0, self.n):
            temp = input().split(" ")
            puz.append(temp)
        return puz
    
    def isGoal(self, start, goal):
        """ Calculates the different between the given puzzles """
        temp = 0
        for i in range(0,self.n):
            for j in range(0,self.n):
                if start[i][j] != goal[i][j] and start[i][j] != '_':
                    temp += 1
        return temp == 0
    
    def printSolution(self, node_list):
        for node in node_list.solution:
            print("\n")
            node.printMatrix()

    def process(self):
        """ Accept Start and Goal Puzzle state"""
        print("Enter the start state matrix \n")
        start = self.accept()
        print("Enter the goal state matrix \n")        
        goal = self.accept()
        
        start = Node(start, 0)
        self.open.append(start)
        print("\n\n")
        while True:
            cur = self.open[0]
            """ If the difference between current and goal node is 0 we have reached the goal node"""
            if(self.isGoal(cur.data, goal)):
                cur.solution = cur.solution + [cur.data]
                self.printSolution(cur)
                break
            for i in cur.generate_child():
                self.open.append(i)
            self.closed.append(cur)
            del self.open[0]

puz = Puzzle(3)
puz.process()