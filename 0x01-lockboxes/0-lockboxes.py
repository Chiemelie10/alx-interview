#!/usr/bin/python3
"""This module defines the function canUnlockAll."""


def canUnlockAll(boxes):
    """
    - This function returns True if the accessible keys in each
    box can unlock all the boxes.
    - It returns false if one or more boxes cannot be unlocked.
    - The function parameter 'boxes' is a list of list.
    - The box at the index of zero (0) is unlocked.
    - All keys will be postive integers
    - A key with the same number as a box (box index) opens that box.
    """

    if len(boxes) <= 1:
        return True

    required_keys = set(range(1, len(boxes)))
    provided_keys = set()

    for idx, box in enumerate(boxes):
        current_required_keys = required_keys.copy()

        if idx > 0:
            current_required_keys.remove(idx)

        for key in box:
            if key in current_required_keys:
                provided_keys.add(key)

    return required_keys == provided_keys
