# First-Order Predicate Logic Implementation

"""
First-Order Predicate Logic (FOPL) Implementation

Here is a simple Python program to implement a basic First Order Predicate Logic
(FOPL) related problem using facts and rules.

We will solve a common example:
-> All men are mortal
-> Socrates is a man
-> Therefore, Socrates is mortal
"""

facts = {
    "Man(Socrates)"
}

def apply_rules(facts):
    new_facts = set()
    for fact in facts:
        if fact.startswith("Man("):
            person = fact[4:-1]  # Extract the name
            new_facts.add(f"Mortal({person})")  # Add the conclusion
    return new_facts

def main():
    print("Initial Facts:", facts)
    new_facts = apply_rules(facts)
    facts.update(new_facts)  # Update the facts with new derived facts
    print("Derived Facts:", new_facts)
    print("Final Facts:", facts)
    
if __name__ == "__main__":
    main()
    
    


# Output:
# Initial Facts: {'Man(Socrates)'}
# Derived Facts: {'Mortal(Socrates)'}
# Final Facts: {'Man(Socrates)', 'Mortal(Socrates)'}