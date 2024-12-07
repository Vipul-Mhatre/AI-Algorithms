import heapq

class UniformCostSearch:
    def __init__(self, graph):
        self.graph = graph
    
    def search(self, start, goal):
        frontier = []
        heapq.heappush(frontier, (0, start))  
        costs = {start: 0}
        parent = {start: None}
        
        while frontier:
            current_cost, current_node = heapq.heappop(frontier)
            
            if current_node == goal:
                path = []
                while current_node is not None:
                    path.append(current_node)
                    current_node = parent[current_node]
                return current_cost, path[::-1] 
        
            for neighbor, cost in self.graph[current_node].items():
                new_cost = current_cost + cost
                if neighbor not in costs or new_cost < costs[neighbor]:
                    costs[neighbor] = new_cost
                    parent[neighbor] = current_node
                    heapq.heappush(frontier, (new_cost, neighbor))
        
        return float("inf"), []  

if __name__ == "__main__":
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    
    ucs = UniformCostSearch(graph)
    start = 'A'
    goal = 'D'
    cost, path = ucs.search(start, goal)
    
    print(f"Total cost: {cost}")
    print(f"Path: {' -> '.join(path)}")