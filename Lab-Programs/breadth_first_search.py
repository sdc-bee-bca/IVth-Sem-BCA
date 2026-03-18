"""
Breadth First Search (BFS) implementation in Python

Statement: Implement the breadth first search algorithm for traversing or 
searching tree or graph data structures.
"""

from collections import deque

def breadth_first_search(graph: dict, start_node: str) -> list:
    """
    Perform breadth first search on a graph starting from a given node.
    
    Args:
        graph: Dictionary representing the graph (adjacency list)
        start: Starting node for BFS
    
    Returns:
        List of nodes in BFS order
    """
    visited = set() # Set to keep track of visited nodes
    queue = deque([start_node]) # Queue for BFS, initialized with the starting node
    visited.add(start_node) # Mark the starting node as visited
    bfs_order = [] # List to store the order of nodes visited in BFS
    
    # Loop until the queue is empty
    while queue:
        node = queue.popleft() # Dequeue a node from the front of the queue
        bfs_order.append(node) # Add the dequeued node to the BFS order list
        
        # Iterate through the neighbors of the current node
        for neighbor in graph[node]:
            if neighbor not in visited: # If the neighbor has not been visited
                visited.add(neighbor) # Mark the neighbor as visited
                queue.append(neighbor) # Enqueue the neighbor for future exploration
    
    # Return the list of nodes in the order they were visited
    return bfs_order


def main():
    """
    Main function to demonstrate breadth first search on a sample graph.
    
    Args:
        None
        
    Returns:
        None
    """
    # Define a sample graph as an adjacency list
    graph = {
        'S': ['A', 'B'],
        'A': ['C', 'D'],
        'B': ['G', 'H'],
        'C': ['E', 'F'],
        'D': [],
        'G': ['I'],
        'H': [],
        'E': ['K'],
        'F': [],
        'I': [],
        'K': []
    }
    
    start_node = 'S'
    result = breadth_first_search(graph, start_node)
    print(f"BFS traversal starting from node {start_node}: {result}")


if __name__ == "__main__":
    main()


# Output:

# BFS traversal starting from node S: ['S', 'A', 'B', 'C', 'D', 'G', 'H', 'E', 'F', 'I', 'K']