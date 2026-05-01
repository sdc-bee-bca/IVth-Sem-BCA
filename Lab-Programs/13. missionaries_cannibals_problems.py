# Missionaries and Cannibals Problem

"""
Problem Statement:
The Missionaries and Cannibals problem is a classic problem in artificial intelligence
and problem-solving. The problem involves three missionaries and three cannibals who 
need to cross a river using a boat that can carry at most two people. The challenge 
is to find a way to get all the missionaries and cannibals across the river without 
ever leaving more cannibals than missionaries on either side of the river, as this 
would lead to the missionaries being eaten.

Simple Explanation
    -> 3 Missionaries and 3 Cannibals must cross the river.
    -> Boat can carry maximum 2 persons.
    -> Cannibals should never outnumber missionaries on either side.
    -> BFS is used to find the shortest solution.

Possible Boat Moves
    The boat can carry:
    -> 1 Missionary (1M)
    -> 2 Missionaries (2M)
    -> 1 Cannibal (1C)
    -> 2 Cannibals (2C)
    -> 1 Missionary + 1 Cannibal (1M,1C)
"""

from collections import deque

def is_valid(m_left, c_left, m_right, c_right):
    if (m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0):
        return False
    if (m_left > 3 or c_left > 3 or m_right > 3 or c_right > 3):
        return False
    if (m_left > 0 and m_left < c_left):
        return False
    if (m_right > 0 and m_right < c_right):
        return False
    return True

def bfs():
    # (M_left, C_left, boat_position, M_right, C_right)
    initial_state = (3, 3, 0, 0, 0)  
    goal_state = (0, 0, 1, 3, 3)
    
    queue = deque([(initial_state, [])])  # (current_state, path_to_reach_state)
    visited = set()
    
    while queue:
        (state, path) = queue.popleft()
        m_left, c_left, boat_position, m_right, c_right = state
        
        if state == visited:
            continue
        visited.add(state)
        
        if state == goal_state:
            return path + [state]
        
        moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
        
        for m_move, c_move in moves:
            if boat_position == 0:  # Boat on the left side
                new_state = (m_left - m_move, c_left - c_move, 1, 
                             m_right + m_move, c_right + c_move)
            else:  # Boat on the right side
                new_state = (m_left + m_move, c_left + c_move, 0, 
                             m_right - m_move, c_right - c_move)
            
            if is_valid(*new_state[:2], *new_state[3:]):
                queue.append((new_state, path + [state]))
                
    return None

def main():
    solution = bfs()
    if solution:
        print("Solution found:")
        for step in solution:
            print(step)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
    
    


# Output:
# Solution found:
# (3, 3, 0, 0, 0)
# (3, 1, 1, 0, 2)
# (3, 2, 0, 0, 1)
# (3, 0, 1, 0, 3)
# (3, 1, 0, 0, 2)
# (1, 1, 1, 2, 2)
# (2, 2, 0, 1, 1)
# (0, 2, 1, 3, 1)
# (0, 3, 0, 3, 0)
# (0, 1, 1, 3, 2)
# (1, 1, 0, 2, 2)
# (0, 0, 1, 3, 3)