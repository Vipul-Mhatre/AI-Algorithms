def depth_limited_search(graph, start, goal, limit):

    def dls_helper(node, goal, limit, visited, path):
        if limit < 0:
            return None  

        visited.add(node)
        path.append(node)

        if node == goal:
            return path  
        
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                result = dls_helper(neighbor, goal, limit - 1, visited, path)
                if result is not None:
                    return result
        
        path.pop()  
        return None

    visited = set() 
    return dls_helper(start, goal, limit, visited, [])

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['G'],
        'F': [],
        'G': []
    }

    start = 'A'
    goal = 'G'
    limit = 3  # Depth limit

    path = depth_limited_search(graph, start, goal, limit)
    if path:
        print(f"Path to goal: {path}")
    else:
        print(f"No path found within depth limit of {limit}")