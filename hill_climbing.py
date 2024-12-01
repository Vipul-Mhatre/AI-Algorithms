import random

distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
def total_distance(path):
    total = 0
    for i in range(len(path) - 1):
        total += distance_matrix[path[i]][path[i+1]]
    total += distance_matrix[path[-1]][path[0]]  
    return total
def hillclimbing(num_cities, max_iterations=10000):
    current_path = list(range(num_cities)) 
    current_distance = total_distance(current_path) 
    for _ in range(max_iterations):
        neighbor_path = current_path.copy()
        i, j = random.sample(range(num_cities), 2)
        neighbor_path[i], neighbor_path[j] = neighbor_path[j], neighbor_path[i]
        neighbor_distance = total_distance(neighbor_path)
        
        if neighbor_distance < current_distance:
            current_path = neighbor_path
            current_distance = neighbor_distance
    return current_path

num_cities = 4  
solution = hillclimbing(num_cities)
print("Optimal path is:", solution)
print("Total distance is:", total_distance(solution))