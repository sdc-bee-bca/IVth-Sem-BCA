# Traveling Salesman Problem (TSP) using brute-force approach

"""
Problem Statement:
The Traveling Salesman Problem (TSP) is a classic optimization problem 
in which a salesman mustvisit a set of cities exactly once and return to 
the starting city, while minimizing the total travel cost.The cost of travel 
between each pair of cities is given in the form of a cost matrix.In this 
implementation, we will use a brute-force approach to solve the TSP. 
We will generate all possible permutations of the cities (except the starting city) 
and calculate the total cost for each permutation. Finally, we will determine the 
minimum cost and the corresponding route.
"""

import itertools

def tsp(cost_matrix, start_city):
    n = len(cost_matrix) 
    cities = list(range(n))
    cities.remove(start_city)
    
    min_path_cost = float('inf')
    best_route = []
    
    for perm in itertools.permutations(cities):
        current_cost = 0
        previous_city = start_city
        for city in perm:
            current_cost += cost_matrix[previous_city][city] 
            previous_city = city
            
        current_cost += cost_matrix[previous_city][start_city]
        
        if current_cost < min_path_cost:
            min_path_cost = current_cost
            best_route = [start_city] + list(perm) + [start_city]
        
    return min_path_cost, best_route
    
def main():
    cost_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]  
    star_city = 0 
    min_cost, route = tsp(cost_matrix, star_city)
    print(f"Minimum cost: {min_cost}")
    print(f"Best route: {route}")


if __name__ == "__main__":
    main()
    
    


# Output:
# Minimum cost: 80
# Best route: [0, 1, 3, 2, 0]