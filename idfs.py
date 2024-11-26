def iterative_dfs(graph, start):
    visited = set()  
    stack = [start] 
    finalOrder = [] 
    
    while stack:
        node = stack.pop() 
        
        if node not in visited:
            visited.add(node) 
            finalOrder.append(node)  
            
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

    return finalOrder

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

result = iterative_dfs(graph, 'A')
print("Order of visit:", result)

# Order of visit: ['A', 'B', 'D', 'E', 'F', 'C']