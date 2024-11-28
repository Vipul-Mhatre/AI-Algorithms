class Node:
    def __init__(self, state, parent=None):
        self.state = state 
        self.parent = parent  
        self.h = 0  

    def __lt__(self, other):
        return self.h < other.h

class GreedyBestFirstSearch:
    def __init__(self, start, goal, heuristic):
        self.start = start
        self.goal = goal
        self.heuristic = heuristic  # mapping states to heuristic values
        
    def search(self):
        open_list = [Node(self.start)]
        open_list[0].h = self.heuristic(self.start) 
        closed_list = set()

        while open_list:
            open_list.sort()
            
            current_node = open_list.pop(0)
            
            if current_node.state == self.goal:
                return self.reconstruct_path(current_node)
            
            closed_list.add(current_node.state)
            neighbors = self.expand(current_node)
            
            for neighbor in neighbors:
                if neighbor.state not in closed_list:
                    neighbor.h = self.heuristic(neighbor.state)  
                    open_list.append(neighbor) 

        return None  

    def expand(self, node):
        """Generate neighbors for a node (this is a simple example)"""
        neighbors = []
        for delta in [-1, 1]:
            neighbor_state = node.state + delta
            neighbors.append(Node(neighbor_state, node))
        return neighbors

    def reconstruct_path(self, node):
        """Reconstruct the path from start to goal"""
        path = []
        while node:
            path.append(node.state)
            node = node.parent
        return path[::-1] 
    
def heuristic(state):
    return abs(state - 10) 

start_state = 0
goal_state = 10
gbfs = GreedyBestFirstSearch(start_state, goal_state, heuristic)
path = gbfs.search()

if path:
    print("Path to goal:", path)
else:
    print("No path found.")