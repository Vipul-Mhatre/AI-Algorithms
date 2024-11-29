import heapq

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
        self.heuristic = heuristic  
        
    def search(self):
        open_list = []
        start_node = Node(self.start)
        start_node.h = self.heuristic(self.start)  
        heapq.heappush(open_list, start_node)
        closed_list = set()

        while open_list:
            current_node = heapq.heappop(open_list)
            
            if current_node.state == self.goal:
                return self.reconstruct_path(current_node)
            
            closed_list.add(current_node.state)
            neighbors = self.expand(current_node)
            
            for neighbor in neighbors:
                if neighbor.state not in closed_list:
                    neighbor.h = self.heuristic(neighbor.state)  
                    heapq.heappush(open_list, neighbor)  

        return None  

    def expand(self, node):
        neighbors = []
        for delta in [-1, 1]:
            neighbor_state = node.state + delta
            neighbors.append(Node(neighbor_state, node))
        return neighbors

    def reconstruct_path(self, node):
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