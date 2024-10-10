#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    """Determines if all boxes can be opened."""
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = [0]

    while keys:
        current_key = keys.pop()
        for key in boxes[current_key]:
            if not unlocked[key]:
                unlocked[key] = True
                keys.append(key)

    return all(unlocked)
