# Alpha-Beta Pruning

"""
Problem Statement:
Alpha–Beta Pruning is an optimization technique for the Minimax algorithm used 
in two-player games like Chess and Tic-Tac-Toe.It reduces the number of nodes 
evaluated in the game tree by eliminating branches that cannot affect the 
final decision.

Key Concepts
-> Alpha (α) → Best value that the maximizing player can guarantee.
-> Beta (β) → Best value that the minimizing player can guarantee.
-> Pruning Condition:
    When β ≤ α, further exploration of that branch is stopped. 
"""

import math

def minimax(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
    if depth == 3:
        return values[nodeIndex]
    
    if maximizingPlayer:
        maxEval = -math.inf
        for i in range(2):
            eval = minimax(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            
            if beta <= alpha:
                break
            
        return maxEval
    
    else:
        minEval = math.inf
        for i in range(2):
            eval = minimax(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            
            if beta <= alpha:
                break
            
        return minEval
    
def main():
    values = [3, 5, 6, 9, 1, 2, 0, -1]
    result = minimax(0, 0, True, values, -math.inf, math.inf)
    print(f"The optimal value is: {result}")
    
if __name__ == "__main__":
    main()
    
    


# Output:
# The optimal value is: 5