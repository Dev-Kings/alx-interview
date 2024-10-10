#!/usr/bin/python3

def canUnlockAll(boxes):
    """Determines if all boxes can be opened."""
    n = len(boxes)
    unlocked = [False] * n  # Track unlocked boxes
    unlocked[0] = True  # The first box is unlocked
    keys = [0]  # Start with keys from the first box

    while keys:
        current_key = keys.pop()  # Get the next key
        for key in boxes[current_key]:  # Check which boxes can be unlocked
            if not unlocked[key]:  # If the box is not unlocked
                unlocked[key] = True  # Unlock it
                keys.append(key)  # Add the key to the list

    return all(unlocked)  # Return True if all boxes are unlocked
