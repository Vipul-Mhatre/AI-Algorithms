import random

goal = "cake"
population = ["make", "bake", "sake", "take"]
mutation_rate = 0.1  # 10% chance of mutation

# Count how many characters in the word match the goal word at the same position
def calculate_fitness(word):
    score = 0
    for i in range(len(goal)):
        if word[i] == goal[i]:
            score += 1
    return score

# Pick the two best words from the population based on fitness
def select_parents(population):
    fitness_scores = []  
    for word in population:
        score = calculate_fitness(word)  
        fitness_scores.append([word, score])  
    
    for i in range(len(fitness_scores)):
        for j in range(i + 1, len(fitness_scores)):
            if fitness_scores[i][1] < fitness_scores[j][1]: 
                fitness_scores[i], fitness_scores[j] = fitness_scores[j], fitness_scores[i]
   
    parent1 = fitness_scores[0][0] 
    parent2 = fitness_scores[1][0]
    return parent1, parent2

#Crossover function
def crossover(parent1, parent2):
    child = ""
    for i in range(len(goal)):
        if random.random() < 0.5:
            child += parent1[i] 
        else:
            child += parent2[i]  
    return child

#Mutation function
def mutate(word):
    word = list(word)
    for i in range(len(word)):
        if random.random() < mutation_rate:  
            word[i] = random.choice("abcdefghijklmnopqrstuvwxyz")  
    return "".join(word)

generation = 1
while True:
    print(f"Generation {generation}: {population}")
    
    if goal in population:
        print(f"Goal reached in generation {generation}: {goal}")
        break
    
    parent1, parent2 = select_parents(population)
    
    next_population = []
    for _ in range(len(population)):
        child = crossover(parent1, parent2)
        child = mutate(child)
        next_population.append(child)
    
    population = next_population
    generation += 1