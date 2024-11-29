import heapq

grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def is_valid_move(x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0

def heuristic(start, goal):
    return abs(start[0] - goal[0]) + abs(start[1] - goal[1])

def a_star(start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))  
    g_score = {start: 0}
    came_from = {}  
    
    while open_list:
        _, current = heapq.heappop(open_list)
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  
        
        for move in moves:
            neighbor = (current[0] + move[0], current[1] + move[1])
            if is_valid_move(neighbor[0], neighbor[1]):
                tentative_g_score = g_score[current] + 1  
                
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score = tentative_g_score + heuristic(neighbor, goal)
                    heapq.heappush(open_list, (f_score, neighbor))
    
    return None  

start = (0, 0)  
goal = (4, 4)   
path = a_star(start, goal)

if path:
    print("Path found:", path)
else:
    print("No path found.")