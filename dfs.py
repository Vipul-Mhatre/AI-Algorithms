def dfs(graph, start):
    visited = set()  
    finalOrder = []  
    
    def dfs_helper(node):
        visited.add(node) 
        finalOrder.append(node) 
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs_helper(neighbor)  
    
    dfs_helper(start)
    return finalOrder

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

result = dfs(graph, 'A')
print("Order of visit:", result)

# Order of visit: ['A', 'B', 'D', 'E', 'F', 'C']