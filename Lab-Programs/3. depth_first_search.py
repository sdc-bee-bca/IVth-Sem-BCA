"""
Depth First Search (DFS) Implementation in Python

Statement: Implement the depth first search algorithm for traversing or 
searching tree or graph data structures.
"""

def dfs(graph: dict, node: str, visited: set) -> list:
    """
    Depth First Search implementation using recursion
    
    Args:
        graph: Dictionary representing the graph (adjacency list)
        node: Current node being visited
        visited: Set to track visited nodes
    
    Returns:
        List of nodes in DFS order
    """
    # Check if the current node has not been visited
    if node not in visited:
        visited.add(node) # Mark the current node as visited
        dfs_order = [node] # Initialize DFS order list with the current node
        
        # Recursively visit each neighbor of the current node
        for neighbor in graph[node]:
            # Extend the DFS order list with the results from the recursive call
            dfs_order.extend(dfs(graph, neighbor, visited)) 
        
        return dfs_order


def main():
    """
    Main function to demonstrate depth first search on a sample graph.
    
    Args:
        None
        
    Returns:
        None
    """
    # Sample graph as adjacency list
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
    visited = set() # Set to keep track of visited nodes
    dfs_result = dfs(graph, 'S', visited) # Perform DFS starting from node 'S'
    print(f'DFS traversal starting from node S: {dfs_result}') # Print the DFS result


if __name__ == "__main__":
    main()


# Output:

# DFS traversal starting from node S: ['S', 'A', 'C', 'E', 'K', 'F', 'D', 'B', 'G', 'I', 'H']