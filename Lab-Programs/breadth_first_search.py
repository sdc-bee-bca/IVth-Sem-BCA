# Breadth First Search (BFS) implementation in Python

# Statement: Implement the breadth first search algorithm for traversing or 
# searching tree or graph data structures.


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
    visited = set()
    queue = deque([start_node])
    visited.add(start_node)
    bfs_order = []
    
    while queue:
        node = queue.popleft()
        bfs_order.append(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return bfs_order


def main():
    """
    Main function to demonstrate breadth first search on a sample graph.
    
    Args:
        None
        
    Returns:
        None
    """
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
