# Monkey and Banana Problem

"""
Problem Statement:
The Monkey and Banana problem is a classic problem in artificial intelligence 
and problem-solving.In this problem, a monkey is in a room with a box and 
a banana hanging from the ceiling.The monkey wants to get the banana, but it 
cannot reach it directly. The monkey can move around the room, push the box, 
and climb on it to reach the banana. The objective is to find a sequence of 
actions that allows the monkey to get the banana. The actions available to the monkey are:
1. A monkey is in a room.
2. Bananas are hanging from the ceiling.
3. A chair (or box) is in the room.
4. The monkey must move the chair under the bananas, climb it, and grab the bananas.
"""

# Initial State
monkey_position = "door"
box_position = "window"
banana_position = "center"
monkey_on_box = False
has_banana = False

print("Initial State:")
print(f"Monkey is at the {monkey_position}")
print(f"Box is at the {box_position}")
print(f"Banana is at the {banana_position}")
print()

# Step 1: Monkey moves to the box
monkey_position = box_position
print("Step 1: Monkey moves to the box")

# Step 2: Monkey pushes the box to the center
box_position = "center"
monkey_position = box_position
print("Step 2: Monkey pushes the box to the center")

# Step 3: Monkey climbs on the box
monkey_on_box = True
print("Step 3: Monkey climbs on the box")

# Step 4: Monkey grabs the banana
if monkey_on_box and monkey_position == banana_position:
    has_banana = True
    print("Step 4: Monkey grabs the banana")
    
print()
print("Final State:")
print(f"Has the monkey got the banana? {'Yes' if has_banana else 'No'}")



# Output:
# Initial State:
# Monkey is at the door
# Box is at the window
# Banana is at the center

# Step 1: Monkey moves to the box
# Step 2: Monkey pushes the box to the center
# Step 3: Monkey climbs on the box
# Step 4: Monkey grabs the banana

# Final State:
# Has the monkey got the banana? Yes