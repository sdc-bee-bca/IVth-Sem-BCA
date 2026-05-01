# Hill Climbing Algorithm

"""
Hill Climbing Algorithm Implementation

Hill climbing is a heuristic search algorithm that belongs to the family of local 
search methods. It is designed to solve problems where the goal is to find an optimal
(or nearoptimal) solution by iteratively moving from the current state to a better 
neighboring state, according to a heuristic or evaluation function.

Hill climbing follows these steps:
1. Initial State: Start with an arbitrary or random solution (initial state).
2. Neighboring States: Identify neighboring states of the current solution by making
small adjustments (mutations or tweaks).
3. Move to Neighbor: If one of the neighboring states offers a better solution 
(according to some evaluation function), move to this new state.
4. Termination: Repeat this process until no neighboring state is better than the 
current one. At this point, we have reached a local maximum or minimum. 
"""

def objective(x):
    return -x**2 + 4*x  # Example objective function (a parabola)

def hill_climbing(start, step_size = 1):
    current = start
    while True:
        neighbor1 = current + step_size
        neighbor2 = current - step_size
        
        best_neighbor = current
        if objective(neighbor1) > objective(best_neighbor):
            best_neighbor = neighbor1
        
        if objective(neighbor2) > objective(best_neighbor):
            best_neighbor = neighbor2
            
        if best_neighbor == current:
            return current  # No better neighbor found, return current solution
        
        current = best_neighbor  # Move to the better neighbor
        
def main():
    start = 0  # Starting point
    solution = hill_climbing(start)
    print(f"Optimal solution found: {solution}")
    print(f"Maximum value of objective function: {objective(solution)}")
    
if __name__ == "__main__":
    main()
    
    


# Output:
# Optimal solution found: 2
# Maximum value of objective function: 4