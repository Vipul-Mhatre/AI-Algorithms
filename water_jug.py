def fill_jug_a(p, q, cap_a):
    return cap_a, q  

def fill_jug_b(p, q, cap_b):
    return p, cap_b 

def empty_jug_a(p, q):
    return 0, q  

def empty_jug_b(p, q):
    return p, 0  

def transfer_b_to_a_completely(p, q, cap_a):
    return p + q, 0

def transfer_a_to_b_completely(p, q, cap_b):
    return 0, p + q

def transfer_b_to_a_partially(p, q, cap_a):
    transfer_amount = min(q, cap_a - p)
    return p + transfer_amount, q - transfer_amount

def transfer_a_to_b_partially(p, q, cap_b):
    transfer_amount = min(p, cap_b - q)
    return p - transfer_amount, q + transfer_amount

def solve_water_jug(cap_a, cap_b, goal):
    p, q = 0, 0
    print(f"Initial state: P={p}, Q={q}")
    p, q = fill_jug_b(p, q, cap_b)
    print(f"After Rule 2: P={p}, Q={q}")
    p, q = transfer_b_to_a_completely(p, q, cap_a)
    print(f"After Rule 5: P={p}, Q={q}")
    p, q = fill_jug_b(p, q, cap_b)
    print(f"After Rule 2: P={p}, Q={q}")
    p, q = transfer_b_to_a_partially(p, q, cap_a)
    print(f"After Rule 7: P={p}, Q={q}")
    p, q = empty_jug_a(p, q)
    print(f"After Rule 3: P={p}, Q={q}")
    p, q = transfer_b_to_a_completely(p, q, cap_a)
    print(f"After Rule 5: P={p}, Q={q}")

    if p == goal:
        print(f"Goal state reached: P={p}, Q={q}")
    else:
        print("Failed to reach goal state.")

print("Water Jug Problem")
cap_a = int(input("Enter the capacity of Jug A: "))
cap_b = int(input("Enter the capacity of Jug B: "))
goal = int(input(f"Enter the goal for Jug A (0 to {cap_a}): "))

if goal > cap_a or goal < 0:
    print("Invalid goal! Goal must be between 0 and Jug A's capacity.")
    
solve_water_jug(cap_a, cap_b, goal)