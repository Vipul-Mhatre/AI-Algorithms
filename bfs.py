def bfs(graph, start):
    queue = [start]
    visited = set()
    finalOrder = []
    
    while queue:
        node = queue.pop(0)

        if node not in visited:
            visited.add(node)  
            finalOrder.append(node)  
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    
    return finalOrder

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

result = bfs(graph, 'A')
print("Order of visit:", result)

# Order of visit: ['A', 'B', 'C', 'D', 'E', 'F']