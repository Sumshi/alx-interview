#!/usr/bin/python3
"""
Lockboxes checks
Type of boxes == list
if boxes == list, return true
type of box content == list, continue
if key is in free keys or key is in used keys, skip
if key value is >= length of boxes, skip
"""


def canUnlockAll(boxes):
    """
    A function that returns True if all boxes can be opened, else return False
    """
    if type(boxes) is not list:
        return False
    if len(boxes) == 0:
        return False
    if len(boxes) == 1:
        return True

    free_keys = [0]  # First key is free
    used_keys = []  # No keys used yet

    for key in free_keys:
        for box in boxes[key]:
            if box not in free_keys:
                if box not in used_keys:
                    if box < len(boxes):
                        free_keys.append(box)
        used_keys.append(key)

    if len(free_keys) == len(boxes):
        return True
    else:
        return False
