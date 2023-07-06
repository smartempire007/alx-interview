#!/usr/bin/python3
"""A python module that determines if all boxes can be opened
   from a list of lists
"""


def canUnlockAll(boxes):
    """a function that determines if all the
    boxes can be opened"""
    keys = set([0])
    unlocked = []
    boxes_copy = boxes[:]

    while True:
        try:
            key = keys.pop()
            keys.update(boxes_copy[key])
            unlocked.append(boxes_copy[key])
            boxes_copy[key] = []
        except KeyError:
            break

    for box in boxes:
        if box not in unlocked:
            return False
    return True
