# Forward Chaining Algorithm

"""
Forward Chaining Algorithm Implementation

Forward chaining is a problem-solving approach used in artificial intelligence and logic programming. It starts with the available facts and applies inference rules to derive new facts until a goal is reached.

The algorithm follows these steps:
1. Initialize: Start with the known facts and rules.
2. Apply Rules: For each rule, check if its conditions are satisfied by the current set of facts.
3. Derive New Facts: If a rule's conditions are met, add its conclusion to the set of known facts.
4. Repeat: Continue applying rules until no new facts can be derived or the goal is achieved.
"""

# Knowledge Base (Rules)
# Format: (conditions, conclusion)
rules = [
 (["A", "B"], "C"),
 (["C"], "D"),
 (["D"], "E")
]
# Initial Facts
facts = ["A", "B"]

def forward_chaining(rules, facts):
    inferred = True
    while inferred:
        inferred = False
        for conditions, conclusion in rules:
            if all(condition in facts for condition in conditions):
                if conclusion not in facts:
                    facts.append(conclusion)
                    print(f"Inferred: {conclusion} from {conditions}")
                    inferred = True

    return facts

def main():
    print("Initial Facts:", facts)
    final_facts = forward_chaining(rules, facts)
    print("Final Facts:", final_facts)

if __name__ == "__main__":
    main()
    


# Output:
# Initial Facts: ['A', 'B']
# Inferred: C from ['A', 'B']
# Inferred: D from ['C']
# Inferred: E from ['D']
# Final Facts: ['A', 'B', 'C', 'D', 'E']