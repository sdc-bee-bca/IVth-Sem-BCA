"""
A* Search Implementation in Python

Statement: Implement the A* search algorithm for traversing or 
searching tree or graph data structures.
"""

import heapq

def a_star_search(graph: dict, start: str, goal: str, heuristic: dict) -> list:
    """
    A* Search algorithm implementation
    
    Args:
        graph: Dictionary representing the graph (adjacency list)
        start: Starting node for A* search
        goal: Goal node to reach
        heuristic: Dictionary containing heuristic values for each node
    
    Returns:
        List of nodes representing the path from start to goal
    """
    # Priority queue to store nodes to explore, initialized with the starting node
    open_set = [(0 + heuristic[start], start)]
    print(open_set)
    came_from = {} # Dictionary to reconstruct the path after reaching the goal
    g_score = {node: float('inf') for node in graph} # Cost from start to each node
    print(g_score)
    g_score[start] = 0 # Cost from start to itself is 0
    print(g_score)
    
    while open_set:
        current_f_score, current_node = heapq.heappop(open_set) # Get the node with the lowest f-score
        
        if current_node == goal: # If we have reached the goal, reconstruct and return the path
            path = []
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            path.append(start)
            return path[::-1] # Return reversed path
        
        for neighbor in graph[current_node]: # Explore neighbors of the current node
            tentative_g_score = g_score[current_node] + 1 # Assuming cost between nodes is 1
            
            if tentative_g_score < g_score[neighbor]: # If a better path is found
                came_from[neighbor] = current_node # Update the path to this neighbor
                g_score[neighbor] = tentative_g_score # Update g-score for this neighbor
                f_score = tentative_g_score + heuristic[neighbor] # Calculate f-score
                
                if not any(neighbor == item[1] for item in open_set): # If neighbor is not in open set, add it
                    heapq.heappush(open_set, (f_score, neighbor))
    
    return [] # Return an empty list if there is no path from start to goal

def main():
    """
    Main function to demonstrate A* search on a sample graph.
    
    Args:
        None
    
    Returns:
        None    
    """
    # Sample graph as adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'D'],
        'D': ['B', 'C']
    }
    
    # Sample heuristic values
    heuristic = {
        'A': 5,
        'B': 3,
        'C': 2,
        'D': 1
    }
    
    start = 'A'
    goal = 'D'
    
    path = a_star_search(graph, start, goal, heuristic)
    print("Path from {} to {}: {}".format(start, goal, path))


if __name__ == "__main__":
    main()